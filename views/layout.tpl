<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="fr-FR">
    <head profile="http://gmpg.org/xfn/11">
        <meta http-equiv="cache-control" content="max-age=0" />
        <meta http-equiv="cache-control" content="no-cache" />
        <meta http-equiv="expires" content="0" />
        <meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
        <meta http-equiv="pragma" content="no-cache" />        
        <title>{{title or ""}}</title>
        <link href="/static/jquery/plugins/DataTables/media/css/demo_table.css" rel="stylesheet" media="screen"> 
        <link href="/static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
        %for c in css:
            <link href="/static/css/{{c}}.css" rel="stylesheet" media="screen">        
        %end
        <script type="text/javascript" language="javascript" src="/static/jquery/jquery.min.js"></script>
        <script type="text/javascript" language="javascript" src="/static/jquery/plugins/DataTables/media/js/jquery.dataTables.js"></script>
        <script src="/static/bootstrap/js/bootstrap.min.js"></script>
        <script src="/static/raphael/raphael-min.js"></script>
        <script src="/static/raphael/plugins/justGage/resources/js/justgage.1.0.1.min.js"></script>
    </head>    
    <body>
        %if data["nav"]:
            %include nav.tpl
        %end
        %include
        <script type="text/javascript" charset="utf-8">
            $(document).ready(function() {
                $('.st').tooltip({container:'body'});
            } );
        </script>
    </body>
</html>