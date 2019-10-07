
def first_assert_demo():
    # Przyk³ad u¿ycia instrukcji assert.
    large = 1000
    string = "To jest ci¹g znaków"
    float = 1.0
    broken_int = "To powinna byæ wartoœæ ca³kowita"
    
    assert large > 500
    assert type(string) == type("")
    assert type(float) != type(1)
    assert type(broken_int) == type(4)

def second_assert_demo():
    # Przyk³ad u¿ycia instrukcji assert.
    large = 1000
    string = "To jest ci¹g znaków"
    float = 1.0
    broken_int = "To powinna byæ wartoœæ ca³kowita"
    
    assert large > 500
    assert type(string) == type("")
    assert type(float) != type(1)

    try: 
        assert type(broken_int) == type(4), "broken_int jest niepoprawne"
    except AssertionError, message:
        print "Obs³uga b³êdu. Otrzymany komunikat: %s" % message

print 'W interpreterze wywo³aj first_assert_demo() i second_assert_demo()'
