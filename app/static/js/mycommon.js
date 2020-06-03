function openUrl(url){
    // window.open(url);
    window.open(url, "", "height=800, width=400, top=0, left=0, toolbar=no, menubar=no, scrollbars=no, resizable=no, location=no, status=no");
}


function openUrl_tips(url)
{
    var width=400;
    var height=630;
    var y=(window.screen.availHeight-height/2);
    var x=(window.screen.availWidth-width/2);
    var mywindow=window.open(url,"_blank","height="+height+",width="+width+"toolbar=no, menubar=no, scrollbars=no, resizable=no, location=no, status=no");
    mywindow.moveTo(x/2,y/2);
}

function openUrl_log()
{
    var width=1200;
    var height=700;
    var y=(window.screen.availHeight-height/2);
    var x=(window.screen.availWidth-width/2);

    var url = 'http://' + document.domain + ':' + 4001;
    alert(url);

    var mywindow=window.open(url,"_blank","height="+height+",width="+width+"toolbar=no, menubar=no, scrollbars=no, resizable=no, location=no, status=no");
    mywindow.moveTo(x/2,y/2);
}

function scroll_output(divid) {
    var div = document.getElementById(divid);
    div.scrollTop = div.scrollHeight;
}

function clean_output(divid) {
    var div = document.getElementById(divid);
    div.innerHTML = "";
}
