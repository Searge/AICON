<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" 
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
   xmlns="http://www.w3.org/2000/svg">
  
  <xsl:output method="xml" indent="yes" />

  <xsl:template match="PlayList">
    <svg width="640" height="480">
      <g>
        <xsl:apply-templates select="Track"/>
      </g>
    </svg>
  </xsl:template>

  <xsl:template match="Track">
    <xsl:variable name="y" select="position() * 40"/>
    <text id="text_{position()}" x="10" y="{$y - 5}" 
        font-size="12" font-family="Monospace" text-anchor="left">
      <xsl:value-of select="concat(Artist, ': ', Title)"/>
    </text>
    <rect id="rect_{position()}" x="10" y="{$y}" height="20" width="{@Length}" 
      stroke-width="1" stroke="#000000" fill="#d4ffaa"/>
    <text id="length_{position()}" x="13" y="{$y + 14}" 
      font-size="12" font-family="Monospace" text-anchor="left">
      <xsl:value-of select="@Length"/>
      <xsl:text><![CDATA[ сек.]]></xsl:text>
    </text>
  </xsl:template>

</xsl:stylesheet>