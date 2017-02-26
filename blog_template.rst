|back|

==============
{{.Doc.title}}
==============

{{if .Doc.year}} |posted| {{end}}

{{.Doc.body}}

{{if .Doc.orig_link}} |link| {{end}}

|back| |br|


.. |back| raw:: html

    <div style="float: right;"><a href="/blog">Back to Blog Index</a></div>

.. |br| raw:: html

   <br />

.. |posted| raw:: html

    <span style="font-size: 14px;"><b>Posted:</b> {{.Doc.month_name}} {{.Doc.day}}, {{.Doc.year}}</span>

.. |link| raw:: html

    <i>Original version published at <a href="{{.Doc.orig_link}}">{{.Doc.orig_link}}</a></i>
