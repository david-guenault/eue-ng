<!DOCTYPE html>
<html class="no-js">
    
    <head>
        <title>{{title}}</title>
        <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
            <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
        %for style in css:
        <link href="static/{{style}}" rel="stylesheet" media="screen">
        %end
        %for jscript in js:
        <script src="static/{{jscript}}"></script>
        %end        
    </head>
    
    <body>
        %include nav 
        <div class="container-fluid">
            <div class="row-fluid">
                %include
            </div>
        </div> 
        %for jscript in jslate:
        <script src="static/{{jscript}}"></script>
        %end        
    </body>

</html>