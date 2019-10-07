<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/library">
<html>
<head>
Biblioteczka - <xsl:value-of select="@owner"/>
</head>
<body>
  <h1>Biblioteczka - <xsl:value-of select="@owner"/></h1>
  <xsl:apply-templates/>
</body>
</html>
</xsl:template>

<xsl:template match="book">
  <xsl:apply-templates/>
  <br/>
</xsl:template>

<xsl:template match="title">
<b><xsl:value-of select="."/></b>
</xsl:template>

<xsl:template match="author[1]">
napisana przez <xsl:value-of select="."/>
</xsl:template>

<xsl:template match="author">
, <xsl:value-of select="."/>
</xsl:template>
</xsl:stylesheet>
