function max(a, b) {
    a = parseInt(a.toString().replace('px',''));
    b = parseInt(b.toString().replace('px',''));
    return a > b ? a : b;
}
function resize() {
    w = $(window).width();
    $('.top_center,.bottom_center').css('width', (w-338) + 'px');
    $('.center_center').css('width', (w-78) + 'px');
    h = max($(window).height(), $('.center_center').css('height'))
    $('.rim_center').css('height', (h-76) + 'px');
}
$(function(){
    resize();
    $(window).resize(resize);
});
