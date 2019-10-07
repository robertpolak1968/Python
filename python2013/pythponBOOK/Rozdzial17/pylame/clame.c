#include <stdio.h>
#include <stdlib.h>

#include <lame.h>

#define INBUFSIZE 4096
#define MP3BUFSIZE (int)(1.25 * INBUFSIZE) + 7200

int encode(char *inpath, char *outpath) {
    int status = 0;
    lame_global_flags *gfp;
    int ret_code;
    FILE *infp;
    FILE *outfp;
    short *input_buffer;
    int input_samples;
    char *mp3_buffer;
    int mp3_bytes;

    /* Inicjalizuj bibliotekê. */
    gfp = lame_init();
    if (gfp == NULL) {
        printf("lame_init zwróci³o NULL\n");
        status = -1;
        goto exit;
    }

    /* Ustaw parametry kodowania. */
    ret_code = lame_init_params(gfp);
    if (ret_code < 0) {
        printf("lame_init_params zwróci³o %d\n", ret_code);
        status = -1;
        goto close_lame;
    }

    /* Otwórz plik wej¶ciowy i wyj¶ciowy. */
    infp = fopen(inpath, "rb");
    outfp = fopen(outpath, "wb");

    /* Alokuj bufory. */
    input_buffer = (short*)malloc(INBUFSIZE*2);
    mp3_buffer = (char*)malloc(MP3BUFSIZE);

    /* Czytaj z wej¶cia, koduj i zapisuj na wyj¶cie. */
    do {
        input_samples = fread(input_buffer, 2, INBUFSIZE, infp);
        if (input_samples > 0) {
            mp3_bytes = lame_encode_buffer_interleaved(
                gfp,
                input_buffer,
                input_samples / 2,
                mp3_buffer,
                MP3BUFSIZE
            );
            if (mp3_bytes < 0) {
                printf("lame_encode_buffer_interleaved zwróci³o %d\n", mp3_bytes);
                status = -1;
                goto free_buffers;
            } else if (mp3_bytes > 0) {
                fwrite(mp3_buffer, 1, mp3_bytes, outfp);
            }
        }
    } while (input_samples == INBUFSIZE);

    /* Oczy¶æ bufor z pozosta³ych informacji. */
    mp3_bytes = lame_encode_flush(gfp, mp3_buffer, sizeof(mp3_buffer));
    if (mp3_bytes > 0) {
        printf("writing %d mp3 bytes\n", mp3_bytes);
        fwrite(mp3_buffer, 1, mp3_bytes, outfp);
    }

    /* Czyszczenie. */

free_buffers:
    free(mp3_buffer);
    free(input_buffer);

    fclose(outfp);
    fclose(infp);

close_lame:
    lame_close(gfp);

exit:
    return status;
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("u¿ycie: clame surowyplik plikmp3\n");
        exit(1);
    }
    encode(argv[1], argv[2]);
    return 0;
}

