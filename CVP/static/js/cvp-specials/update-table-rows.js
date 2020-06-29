// Enable pusher logging - don't include this in production
Pusher.logToConsole = true;

var pusher = new Pusher('d98471de37bd168f6edc', {
    cluster: 'ap1'
});

var channel = pusher.subscribe('plate-detection');
channel.bind('add-table-row', function (data) {
    console.log($('#data-table-basic'))
    var row = '<tr'
    if (data['new-approved'])
        row += ' style="cursor: pointer" onclick="window.location=\'' + data['new-url'] + '\';';
    row += '><td class="persianTable">' + data['new-plate'] + '</td>';
    if (data['new-approved'])
        row += '<td><button class="disabled  button-icon-btn btn btn-success success-icon-notika btn-reco-mg"><i class="notika-icon notika-checked"></i></button><p class="hidden">مجاز True</p></td>';
    else
        row += '<td><button class="disabled  button-icon-btn btn btn-danger danger-icon-notika btn-reco-mg"><i class="notika-icon notika-close"></i></button><p class="hidden">False غیر مجاز</p></td>';
    row += '<td class="persianTable">' + data['new-seen-hour'] + ':' + data['new-seen-minute'] + ':' + data['new-seen-second'] + '</td>';
    row += '<td class="persianTable">' + data['new-seen-date'] + '</td></tr>';

    $(row).insertBefore('#data-table-basic > tbody > tr:first');
    alert(JSON.stringify(data));
});
