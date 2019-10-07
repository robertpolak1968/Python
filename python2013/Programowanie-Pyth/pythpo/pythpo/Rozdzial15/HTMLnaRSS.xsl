<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="xml" doctype-system="http://my.netscape.com/publish/formats/rss-0.91.dtd" doctype-public="-//Netscape Communications//DTD RSS 0.91//EN"/> 

<xsl:template match="/">
<rss version="0.91">
<channel>
<xsl:apply-templates select="html/head/title"/>
<link>http://serwer.domena.tld</link>
<description>To jest mój blog. Istnieje wiele innych, ale ten jest moją własnością.</description>
<xsl:apply-templates select="html/body/div[@class='story']"/>
</channel>
</rss>
</xsl:template>

<xsl:template match="head/title">
<title>
<xsl:apply-templates/>
</title>
</xsl:template>

<xsl:template match="div[@class='story']">
<item>
<xsl:apply-templates/>
<link>
http://serwer.domena.tld/mojblog.html#<xsl:value-of select="a/@name"/>
</link>
</item>
</xsl:template>

<xsl:template match="h2">
<title><xsl:apply-templates/></title>
</xsl:template>

<xsl:template match="div[@class='story']/span[@class='content']">
<description>
<xsl:apply-templates/>
</description>
</xsl:template>

<xsl:template match="div[@class='date']"/>
</xsl:stylesheet>
