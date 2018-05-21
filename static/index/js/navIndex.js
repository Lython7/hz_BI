function navIndex(num) {
    var oNav=document.getElementById('navList');
    var aList=oNav.getElementsByTagName('a');
    aList[num].className='active';
}