%rebase layout globals(), title="Calendar", css=["bootstrap/css/bootstrap.min.css", "vendors/fullcalendar/fullcalendar.css", "assets/styles.css", "css/calendar.css"], js=["vendors/modernizr-2.6.2-respond-1.1.0.min.js"], jslate=["vendors/jquery-1.9.1.min.js", "vendors/jquery-ui-1.10.3.js", "bootstrap/js/bootstrap.min.js", "vendors/fullcalendar/fullcalendar.js", "vendors/fullcalendar/gcal.js", "assets/scripts.js","js/calendar.js"]
<div class="span9" id="content">
    <div class="row-fluid">
        <!-- block -->
        <div class="block">
            <div class="navbar navbar-inner block-header">
                <div class="muted pull-left">Calendar</div>
                <div class="pull-right"><span class="badge badge-warning">View More</span>

                </div>
            </div>
            <div class="block-content collapse in">
                <div class="span2">
                    <div id='external-events'>
                    <h4>Draggable Events</h4>
                    <div class='external-event'>My Event 1</div>
                    <div class='external-event'>My Event 2</div>
                    <div class='external-event'>My Event 3</div>
                    <div class='external-event'>My Event 4</div>
                    <div class='external-event'>My Event 5</div>
                    <div class='external-event'>My Event 6</div>
                    <div class='external-event'>My Event 7</div>
                    <div class='external-event'>My Event 8</div>
                    <div class='external-event'>My Event 9</div>
                    <div class='external-event'>My Event 10</div>
                    <div class='external-event'>My Event 11</div>
                    <div class='external-event'>My Event 12</div>
                    <div class='external-event'>My Event 13</div>
                    <div class='external-event'>My Event 14</div>
                    <div class='external-event'>My Event 15</div>
                    <p>
                    <input type='checkbox' id='drop-remove' /> <label for='drop-remove'>remove after drop</label>
                    </p>
                    </div>

                </div>
                <div class="span10">
                    <div id='calendar'></div>
                </div>
            </div>
        </div>
        <!-- /block -->
    </div>
</div>