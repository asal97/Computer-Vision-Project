// Enable pusher logging - don't include this in production
Pusher.logToConsole = true;

var pusher = new Pusher('d98471de37bd168f6edc', {
    cluster: 'ap1'
});

var channel = pusher.subscribe('plate-detection');
channel.bind('add-table-row', function (data) {
    alert(JSON.stringify(data));
});
