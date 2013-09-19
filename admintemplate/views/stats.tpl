%rebase layout globals(), title="Statistics", css=["bootstrap/css/bootstrap.min.css", "bootstrap/css/bootstrap-responsive.min.css", "assets/styles.css", "vendors/morris/morris.css","vendors/morris/morris.css"], js=["vendors/modernizr-2.6.2-respond-1.1.0.min.js"], jslate=["vendors/jquery-1.9.1.min.js", "vendors/jquery.knob.js", "vendors/raphael-min.js", "vendors/morris/morris.min.js", "bootstrap/js/bootstrap.min.js", "vendors/flot/jquery.flot.js", "vendors/flot/jquery.flot.categories.js", "vendors/flot/jquery.flot.pie.js", "vendors/flot/jquery.flot.time.js", "vendors/flot/jquery.flot.stack.js", "vendors/flot/jquery.flot.resize.js", "assets/scripts.js","js/stats.js"]

<div class="span9" id="content">
      <!-- morris stacked chart -->
    <div class="row-fluid">
        <!-- block -->
        <div class="block">
            <div class="navbar navbar-inner block-header">
                <div class="muted pull-left">Morris.js stacked</div>
                <div class="pull-right"><span class="badge badge-warning">View More</span>

                </div>
            </div>
            <div class="block-content collapse in">
                <div class="span12">
                    <div id="hero-area" style="height: 250px;"></div>
                </div>
            </div>
        </div>
        <!-- /block -->
    </div>

    <!-- morris graph chart -->
    <div class="row-fluid section">
         <!-- block -->
        <div class="block">
            <div class="navbar navbar-inner block-header">
                <div class="muted pull-left">Morris.js <small>Monthly growth</small></div>
                <div class="pull-right"><span class="badge badge-warning">View More</span>

                </div>
            </div>
            <div class="block-content collapse in">
                <div class="span12">
                    <div id="hero-graph" style="height: 230px;"></div>
                </div>
            </div>
        </div>
        <!-- /block -->
    </div>

    <!-- morris bar & donut charts -->
    <div class="row-fluid section">
         <!-- block -->
        <div class="block">
            <div class="navbar navbar-inner block-header">
                <div class="muted pull-left">Morris.js</div>
                <div class="pull-right"><span class="badge badge-warning">View More</span>

                </div>
            </div>
            <div class="block-content collapse in">
                <div class="span6 chart">
                    <h5>Devices sold</h5>
                    <div id="hero-bar" style="height: 250px;"></div>
                </div>
                <div class="span5 chart">
                    <h5>Month traffic</h5>
                    <div id="hero-donut" style="height: 250px;"></div>    
                </div>
            </div>
        </div>
        <!-- /block -->
    </div>

    <!-- jQuery knobs -->
    <div class="row-fluid section">
         <!-- block -->
        <div class="block">
            <div class="navbar navbar-inner block-header">
                <div class="muted pull-left">jQuery Knob</div>
                <div class="pull-right"><span class="badge badge-warning">View More</span>

                </div>
            </div>
            <div class="block-content collapse in">
                <div class="span3">     
                    <input type="text" value="50" class="knob second" data-thickness=".3" data-inputColor="#333" data-fgColor="#30a1ec" data-bgColor="#d4ecfd" data-width="140">
                </div>
                <div class="span3">
                    <input type="text" value="75" class="knob second" data-thickness=".3" data-inputColor="#333" data-fgColor="#8ac368" data-bgColor="#c4e9aa" data-width="140">
                </div>
                <div class="span3">
                    <input type="text" value="35" class="knob second" data-thickness=".3" data-inputColor="#333" data-fgColor="#5ba0a3" data-bgColor="#cef3f5" data-width="140">
                </div>
                <div class="span3">
                    <input type="text" value="85" class="knob second" data-thickness=".3" data-inputColor="#333" data-fgColor="#b85e80" data-bgColor="#f8d2e0" data-width="140">
                </div>
            </div>
        </div>
        <!-- /block -->
    </div>


    <div class="row-fluid">
        <!-- block -->
        <div class="block">
            <div class="navbar navbar-inner block-header">
                <div class="muted pull-left">Bar Chart</div>
                <div class="pull-right"><span class="badge badge-warning">View More</span>

                </div>
            </div>
            <div class="block-content collapse in">
                <div class="span12">
                    <div id="catchart" style="width:100%;height:300px"></div>
                </div>
            </div>
        </div>
        <!-- /block -->
    </div>

    <div class="row-fluid">
        <div class="span6">
            <!-- block -->
            <div class="block">
                <div class="navbar navbar-inner block-header">
                    <div class="muted pull-left">Pie Chart</div>
                </div>
                <div class="block-content collapse in">
                    <div class="span12">
                       <div id="piechart1" style="width:100%;height:200px"></div>
                    </div>
                </div>
            </div>
            <!-- /block -->
        </div>
        <div class="span6">
            <!-- block -->
            <div class="block">
                <div class="navbar navbar-inner block-header">
                    <div class="muted pull-left">Pie Chart</div>
                </div>
                <div class="block-content collapse in">
                    <div class="span12">
                       <div id="piechart2" style="width:100%;height:200px"></div>
                    </div>
                </div>
            </div>
            <!-- /block -->
        </div>
    </div>

    <div class="row-fluid">
        <!-- block -->
        <div class="block">
            <div class="navbar navbar-inner block-header">
                <div class="muted pull-left">Multiple axes</div>
            </div>
            <div class="block-content collapse in">
                <div class="span12">
                    <div id="timechart" style="width:100%;height:400px"></div>
                </div>
            </div>
        </div>
        <!-- /block -->
    </div>

</div>