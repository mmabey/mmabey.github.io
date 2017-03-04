|back|
|js|

=======
|title|
=======

{{if .Doc.year}} |posted| {{end}}

{{.Doc.body}}

{{if .Doc.orig_link}} |link| {{end}}

{{if .Doc.tags}} |entry_tags| {{end}}

|back| |br|

|filter_tags|


.. |back| raw:: html

    <div style="float: right;"><a href="/blog">Back to Blog Index</a></div>

.. |br| raw:: html

   <br />

.. |posted| raw:: html

    <span style="font-size: 14px;"><b>Posted:</b> <span id="month_name"></span> {{.Doc.day}}, {{.Doc.year}}</span><script>fill_month({{.Doc.month}});</script>

.. |link| raw:: html

    <i>Original version published at <a href="{{.Doc.orig_link}}">{{.Doc.orig_link}}</a></i>

.. |title| raw:: html

    {{if .URL.Query.Get "tag" -}}
      Entries with tag:
     {{- range $field, $val := .URL.Query -}}
      {{- if eq $field "tag" -}}
       {{range $tag := $val}} {{$tag}} {{end}}
      {{- end -}}
     {{- end}}
    {{- else -}}
      {{.Doc.title}}
    {{- end}}

.. |entry_tags| raw:: html

    <span style="font-size: 14px;"><b>Tags:</b>
    {{- range $tag := .Doc.tags -}} <a class="tag_link">{{$tag}}</a>, {{- end -}}
    </span>
    <script>convert_tag_links();</script>

.. |js| raw:: html

    <script src="/_static/tag_toggle.js" />

.. |filter_tags| raw:: html

    <script>
    hide_all();
    {{if .URL.Query.Get "tag"}}
     {{- range $field, $val := .URL.Query -}}
      {{- if eq $field "tag" -}}
       {{range $tag := $val}} show_entries_w_tag("{{$tag}}"); {{end}}
      {{- end -}}
     {{- end}}
    {{else}}
     show_entries_w_tag("entry");
    {{end}}
    </script>
