// calculate 10 minutes in milliseconds
_10MINUTES =  5000; //5 seconds for now

// this function return current date and time as formatted string
function getCurrentDate() {
    // create date object
    var currentdate = new Date();

    // this variable will hold a formatted date
    var date = '';

    // append '0' if day is not a two-digits value
    if (currentdate.getDate() < 10) {
        date = '0';
    }

    // append delimiter
    date += currentdate.getDate() + '/';

    // same this month (getMonth() return 0 for January, so we should add 1)
    if ((currentdate.getMonth() + 1) < 10) {
        date += '0'
    }
    date += (currentdate.getMonth() + 1) + '/' + currentdate.getFullYear() + ' ';

    // same with hours
    if (currentdate.getHours() < 10) {
        date += '0'
    }

    date += currentdate.getHours() + ':';

    // same with minutes
    if (currentdate.getMinutes() < 10) {
        date += '0';
    }

    date += currentdate.getMinutes();

    return date;
}

// this function refreshed the page when invoked
function refreshPage() {
    // this is simple hack to reload the page from JavaScript
    // window.location.href contains current URL. When this value is overwritten,
    // JavaScript will force browser to open url in stated variable (window.location.href)
    window.location.href = window.location.href;
}

// this function will be invoked when page will be load
function initPage() {
    // display current date and time
    document.getElementById('last-updated').innerHTML = getCurrentDate();
    // set timeout for 10 minutes to call a function that refreshes the page
    setTimeout(refreshPage, _10MINUTES)
}
