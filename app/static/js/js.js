/**
  * Global vars
  */
var App = {};
var utilVars={projName:'rps'};
function openSupportWindow(){ showWindow('support_window','out/?id=live_support_url',500,560); }
function showCertificate(u){
    u=u||'out/?id=certificates_url';
    showWindow('cert_window',u,500,350);
}
function showSpecialOffer(u){
    u=u||'out/?id=special_offer_url';
    showWindow('spo_window',u,620,620);
}
function showWindow(id,u,w,h){
    if(!utilVars[id] || utilVars[id].closed){
        utilVars[id]=popItUp(u,id,w,h);
    }
    utilVars[id].focus();
}
function popItUp(u,n,w,h){
    var l=(screen.availWidth  - w) / 2, t=(screen.availHeight - h) / 2
        ,op='toolbar=no,location=no,directories=no,status=no,scrollbars=yes,resizable=yes,copyhistory=no,width='+w+',height='+h+',left='+l+',top='+t
        ,n=n||'_blank';
    return window.open(u,n,op);
}
function reloadImageCode(){
    var img=document.getElementById('vcode_img');
    if(!utilVars.imgCodeUrl) utilVars.imgCodeUrl=img.src;
    img.src=utilVars.imgCodeUrl+'?'+Math.random();
}
function popImg(){
    var u='imgs/pills/blisters/'+jQ(this).attr('prod')+'.jpg';
    var h='<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml">'
        +'<head><title></title>'
        +'<style>html,body,table{margin:0;padding:0;height:100%;width:100%;text-align:center}</style>'
        +'</head><body onclick="close();"><table><tr><td><img src="'+u+'" /></td></tr></table></body></html>';
    var wnd=popItUp('about:blank','img_window',520,520);
    wnd.document.write(h);
    wnd.focus();
    return false;
}
function makeBookmark(a){
    var url = window.document.location;
    var title = window.document.title;
    var ua = navigator.userAgent;
    if (ua.search(/Chrome/) > -1) {
        alert("undefine");
        return false;
    }

    else if (ua.search(/MSIE/) > -1) {

        window.external.AddFavorite(location.href, document.title);
    }

    a.href = url;
    a.rel = 'sidebar';
    a.title = title;
    return true;
}


/**
 * switch class in block or several blocks linked by data-bdx-name
 * @param {object} el
 * @param {string} c = [class to switch]
 * @param {bool} close = [just switch off]
 *
 * data-dbx-name - [css selector[,css selector[,css selector[,...]]] | next]
 * data-dbx-close - [true | false]
 */
function classSwitcher(el, c, close) {
    if(!el)
        return null;

    c = c || 'active';
    close = typeof close === 'boolean'? close : (el.dataset.dbxClose==="true");

    var bx = [];
    if(el.dataset.dbxName){
        if(el.dataset.dbxName !== 'next'){
            bx = document.querySelectorAll(el.dataset.dbxName);
        }else{
            bx.push(el.nextElementSibling);
        }
    }
    // switch in linked box
    for(var i=0; i<bx.length;i++){
        if(bx[i]!=el){
            if(close){
                bx[i].classList.remove(c);
            }else{
                bx[i].classList.toggle(c);
            }
        }
    }
    // switch in element
    if(close){
        el.classList.remove(c);
    }else{
        el.classList.toggle(c);
    }
    return 1;
}

/**
 * @param {string} a = [class]
 * @param {bool} c = [close]
 */
function dbx(a,c){
    a = a || '';
    c = c || null;
    var dropBoxes = document.querySelectorAll('.js-classSwitch'+a);
    for(var i=0;i<dropBoxes.length;i++){
        classSwitcher(dropBoxes[i],null,c);
    }
}

var G_device={};
function setViewport() {
    G_device.viewportWidth = (function (win, docElem) {
        var mM = win['matchMedia'] || win['msMatchMedia'], client = docElem['clientWidth'], inner = win['innerWidth'];
        return mM && client < inner && true === mM('(min-width:' + inner + 'px)')['matches'] ? function () {
            return win['innerWidth']
        } : function () {
            return docElem['clientWidth']
        }
    }(window, document.documentElement));
    G_device.viewportHeight = (function (win, docElem) {
        var mM = win['matchMedia'] || win['msMatchMedia'], client = docElem['clientHeight'], inner = win['innerHeight'];
        return mM && client < inner && true === mM('(min-height:' + inner + 'px)')['matches'] ? function () {
            return win['innerHeight']
        } : function () {
            return docElem['clientHeight']
        }
    }(window, document.documentElement));
    G_device.width = G_device.viewportWidth();
    G_device.height = G_device.viewportHeight();
}

function deviceType() {
    if ((G_device.width < 500)) {//xs
        G_device.type = 0;
    } else if ((G_device.width >= 500) && (G_device.width < 768)) {//sm
        G_device.type = 1;
    } else if ((G_device.width >= 768) && (G_device.width <= 1024)) {//md
        G_device.type = 2;
    } else if ((G_device.width >= 1025) && (G_device.width < 1260)) {//lg
        G_device.type = 3;
    } else if (G_device.width >= 1260) {//xl
        G_device.type = 4;
    }
    else {
        G_device.type = 0;
    }
}

setViewport();
deviceType();

/**
 * Find closest parentNode by tagname | className | id
 * @param {object} el = element
 * @param {string} c = [tagname | className | id]
 */
function myClosest(el,c){
    var r = null;
    if(el && c){
        r = (el.closest && (el.closest(c) || el.closest('.'+c) || el.closest('#'+c)))
            || (
                ((el.parentNode.tagName.toLowerCase() === c.toLowerCase() || el.parentNode.classList.contains(c) || el.parentNode.id === '#'+c) && el.parentNode) 
                || (el.parentNode !== document.body && myClosest(el.parentNode,c))
            );
    }
    return r;
}

function SSfn(el){
    var parent;
    parent = myClosest(el,'sexy-select');
    if(parent.querySelector('.sexy-select-selected') != null)
    parent.querySelector('.sexy-select-selected').innerHTML = el.options[el.selectedIndex].innerHTML;
}

function IncDec(el,id){
    var p = el.parentNode.querySelector('input');
    p.value = parseInt(p.value)+id;
    qtyInp(p);
}

function qtyInp(el) {
    var vr = el.value.replace(/[^\d]/g,''),
        val = parseInt(vr !== ''? vr : 1);
    if(val < 1) val = 1;
    if(val > 99) val = 99;
    el.value = val;
}

function Accordeon(element){
        this.el = element;
        this.init();
    }
    Accordeon.prototype = {
        init: function(){
            this.listItems = this.el.querySelectorAll(".accordeon-item");
            this.toggleItem();
        },
        toggleItem: function(){
            var self = this;
            for(var i=0; i<self.listItems.length;i++){
              self.listItems[i].querySelector('.accordeon-text').addEventListener("click",function(e){
                var parent = myClosest(this,'accordeon-item'),
                    nested = parent.querySelector('.accordeon-nested'),
                    Opened = self.el.querySelector('.opened');
                Opened && Opened !== parent && (Opened.querySelector('.accordeon-nested').style.height = 0, Opened.classList.remove('opened'));
                if(!parent.classList.contains("opened")){
                    nested.style.height = nested.scrollHeight + 'px';
                    parent.classList.add("opened");
                } else {               
                    nested.style.height = 0;
                    parent.classList.remove('opened');            
                }
            });
          }
        }
    };

function toggleClassForList(list, select) {
    [].slice.apply(list).forEach(function(item) {
        item.classList.contains('active') && item.classList.remove('active');
    });
    list[select.selectedIndex].classList.add('active');
}


window.addEventListener('DOMContentLoaded',function(){
 
    /**
     * TableDosage
     */
    (function() {
        var blockTablesDosage = document.querySelectorAll('.js-tblProduct');
        var selectDosage = document.getElementById('select-dosage');

        if (blockTablesDosage.length > 0) {
            selectDosage.addEventListener('change', function() {
                toggleClassForList(blockTablesDosage[0].children, selectDosage);
            });
        }
    })();

    /**
     * classSwitchers
     */
    var dropBoxes = document.querySelectorAll('.js-classSwitch');
    for(var i=0;i<dropBoxes.length;i++){
        dropBoxes[i].addEventListener('click',function (event){
  document.querySelectorAll('.js-dropped')[2].classList.add('opened');
    if(window.innerWidth <=1024){
    var form_header = document.getElementsByClassName('form-header-search')[0].querySelectorAll('button[type="submit"]')[0];

    if(form_header.classList.contains('active') == false)
          form_header.classList.add('active');
    else if(form_header.classList.contains('active') == true && (event.target.className == 'close js-classSwitch active' || event.target.className == 'close js-classSwitch')) 
        form_header.classList.remove('active');
    }

            if(event.target.className == 'icon icon-search' || event.target.className == 'btn-submit js-classSwitch')
            event.preventDefault();
            
            event.stopPropagation();
            classSwitcher(this,null);
        });
    }
    dropBoxes = document.querySelectorAll('.js-dbx');
    for(var i=0;i<dropBoxes.length;i++){
        dropBoxes[i].addEventListener('click',function (event){
            event.stopPropagation();
        });
    }
    /**
     * sexy select
     */
    var SS = document.querySelectorAll('.sexy-select select');
    for(var i=0;i<SS.length;i++){
       SS[i].addEventListener('change',function(ev){
           SSfn(this);
       });
       SSfn(SS[i]);
    }
    /**
     * cart QTY
     */
    var qtyI = document.querySelectorAll('.qty .increment');
    var qtyD = document.querySelectorAll('.qty .decrement');
    for(var i=0;i<qtyI.length;i++){
        qtyI[i].addEventListener('click',function(ev){
            ev.preventDefault();
            IncDec(this,1);
        });
    }
    for(var i=0;i<qtyD.length;i++){
        qtyD[i].addEventListener('click',function(ev){
            ev.preventDefault();
            IncDec(this,-1);
        });
    }
    var qty = document.querySelectorAll('.qty input');
    for(var i=0;i<qty.length;i++){
        qty[i].addEventListener('input',function(ev){
            qtyInp(this);
        });
    }
    /**
     * Accordeons
     */
    var accordeons = document.querySelectorAll(".accordeon");
    for(var i=0;i<accordeons.length;i++){
         new Accordeon(accordeons[i]);
    }

    
    (function () {
        const listSelect = [].slice.apply(document.querySelectorAll('.sexy-select select'));
        listSelect.forEach((item) => {
            setSexyValue(item);

            item.addEventListener('change', function () {
                setSexyValue(this);
            })
        });
    })();

    function setSexyValue(select) {
    const text = (select.name === 'language')
        ? select.value.toUpperCase()
        : select.options[select.selectedIndex].innerHTML;
    select.previousElementSibling.innerHTML = text;
    }


function Slider( element ) {
        this.el = document.querySelector( element );
        this.init();
}
Slider.prototype = {
    init: function() {
        var self = this;
        this.links = this.el.querySelectorAll( "#slider-nav a" );
        this.wrapper = this.el.querySelector( ".list-advantages" );
        this.slides = this.wrapper.querySelectorAll('.slide');
        this.updateSlideDimension();
        this.navigate();
        // self.setCurrentLink(this.links);
        window.addEventListener("resize", function (e) {
          e.stopPropagation();
          self.updateSlideDimension();
          self.slide(self.links[0]);
          self.setCurrentLink(self.links[0]);
          self.wrapper.style.left = "-" + self.el.querySelector( ".slide:nth-child(1)" ).offsetLeft + "px";
        }, false);


    },
    navigate: function() {
        for ( var i = 0; i < this.links.length; ++i ) {
            var link = this.links[i];
            this.slide( link );
        }
    },
    slide: function( element ) {
        var self = this;
        element.addEventListener( "click", function( e ) {
            e.preventDefault();
            var a = this;
            self.setCurrentLink(a);
            var index = parseInt( a.getAttribute( "data-slide" ), 10 ) + 1;
            self.currentSlide = self.el.querySelector( ".slide:nth-child(" + index + ")" );
            self.wrapper.style.left = "-" + self.currentSlide.offsetLeft + "px";
        },
        false);
    },
    setCurrentLink: function(link) {
        var parent = link.parentNode;
        var a = link.parentNode.querySelectorAll( "a" );
        link.className = "current";
        for ( var j = 0; j < a.length; ++j ) {
            var cur = a[j];
            if ( cur !== link ) {
                cur.className = "";
            }
        }
    },

    updateSlideDimension:function(){
        var self = this;
         for(var i = 0; i < self.slides.length;i++ ){
            self.slides[i].style.width = self.el.offsetWidth + "px";

        }
    }


};

document.querySelector("#advantages-container") && ( new Slider("#advantages-container"));

});

window.addEventListener('resize',function(ev){
    var t = G_device.type;
    setViewport();
    deviceType();
    if(t !== G_device.type){
        /**
         * .js-classSwitch
         */
        dbx('',true);
    }
});

document.addEventListener('click',function(ev){
    if (ev.target.closest('.input-search')) return;

    if(!ev.target.classList.contains('js-dbx') && !ev.target.classList.contains('js-classSwitch')){
        dbx('.active',true);
    }
});

window.onclick = function(ev){
    
var smart =document.getElementsByClassName('cart-checkout')[0];

    smart_count = ev.target.className,
     smart_contains = smart.getElementsByClassName('list-ordered-products')[0].classList.contains('active');
     if((smart_count == 'total' || smart_count == 'cart-checkout js-classSwitch') && smart_contains == false)
     smart.getElementsByClassName('list-ordered-products')[0].classList.add('active');
      else if((smart_count == 'total' || smart_count == 'cart-checkout js-classSwitch') && smart_contains == true)
      smart.getElementsByClassName('list-ordered-products')[0].classList.remove('active');       
}


function validateForm(form, name, value_data){
    var err = false;
$('.error').remove();
        if($(name).attr('value') == value_data && typeof(value_data) !== 'undefined'){
            $(form).find('input,textarea').each(function(event){
                
            if($(this).attr('name') == 'email' && !isEmail($(this).val()) && $(this).val() !== ""){
                        err = true;
                        $('article').prepend(function(){
                        return '<div class="error">Invalid email</div>';    
               });
            }
            if($(this).val() == '' && $(this).html() == ''){
            var error = 'Fields can not be empty';
                if($(this).attr('name') == 'email')
                    error = 'Invalid email';
            $('article').prepend(function(){
  return '<div class="error">'+error+'</div>';
 });
           err = true;
           return false; 
    }
        });
        }
        if($(name).attr('name') == 'email' && !isEmail($(name).val()))
        {
            $('article').prepend(function() {
  return '<div class="error">Invalid email</div>';
 });
            err = true;
        }

    if (err) return false;

    return true;


}

function isEmail(email){
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

$('article').ready(function()
{

var array = ['contact','account','subscribe','coupon'];

array.forEach(function(data){

 var data_t = data == 'contact' ? 'contact-us' : data;

if($("div").is('.page-'+data_t)){

var value_data;

$('select, input, textarea, button').change(function(event){

        if(validateForm(document.querySelector('article form[action="/'+data+'.php"]'), event.target, value_data));
});

$('select, input, textarea, button').click(function(event){
        if(event.target.type == 'submit' && event.target.id !== '#search_ref' && event.target.className !== 'btn-submit js-classSwitch active' && event.target.className !== 'icon icon-search' && event.target.className !== 'btn-submit js-classSwitch'){
        event.preventDefault();
        if(validateForm(document.querySelector('article form[action="/'+data+'.php"]'), event.target, event.target.value))
           $('form[action="/'+data+'.php"]').submit();
               }
            });
        }    
    });
});