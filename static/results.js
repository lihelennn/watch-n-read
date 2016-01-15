var searchData=function searchData(){
    //console.log("clicking clicking!");
    var dat = $("search");
    var d = dat.val();
    dat.val("");
    $.getJSON("/search",{input:d},function (d){
	       
    });
    };

$('#b').click(displaySearchData);