<!DOCTYPE html>
<html class="js" prefix="og: http://ogp.me/ns#" lang="en"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"><script src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/cbgapi.loaded_2" async=""></script><script async="" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/share"></script><script async="" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/a"></script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="profile" href="https://gmpg.org/xfn/11">
<link rel="pingback" href="https://arkit.co.in/xmlrpc.php">
<style id="wfc-style-fonts-body" data-origin="server">body{font-family:'Source Sans Pro'!important;}</style><style id="wfc-style-fonts-post_content" data-origin="server">section.content .entry-inner p, .page section.content .entry p{font-family:'Poppins'!important;}</style><style id="wfc-style-fonts-post_lists" data-origin="server">section.content .entry li{font-family:'Poppins'!important;}</style><style id="wfc-style-fonts-single_post_title" data-origin="server">.single .post-inner .post-title{font-family:'Roboto Condensed'!important;}</style><style id="wfc-style-fonts-blockquote" data-origin="server">section.content .entry blockquote p, .format-quote .post-format blockquote{font-family:'Source Sans Pro'!important;}</style><style id="wfc-style-fonts-site_title" data-origin="server">header#header .site-title a{font-family:Comic Sans MS,Comic Sans MS,cursive!important;}</style><style id="wfc-style-fonts-menu_items" data-origin="server">nav#nav-header .nav li a{font-family:Comic Sans MS,Comic Sans MS,cursive!important;}</style><style id="wfc-style-fonts-top_menu_items" data-origin="server">nav#nav-topbar .nav li a{font-family:Comic Sans MS,Comic Sans MS,cursive!important;}</style><style id="wfc-style-fonts-footer_credits" data-origin="server">footer#footer #footer-bottom #copyright, footer#footer #footer-bottom #credit{font-family:Courier New,Courier New,Courier,monospace!important;}</style><style id="wfc-style-fonts-site_description" data-origin="server">#header p.site-description{font-family:Courier New,Courier New,Courier,monospace!important;}</style><style id="wfc-style-fonts-post_links" data-origin="server">section.content .entry a, .format-link .post-format p{font-family:'Poppins'!important;}</style><title>AWS EC2 Instance Creation Using Ansible Playbook Automation</title>
<meta name="description" content="AWS EC2 Instance Creation Using Ansible Playbook Automation. Provisioning EC2 instance fron ansible master node using boto &amp; boto3 AWS. Git Clone and use it">
<link rel="canonical" href="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/">
<meta property="og:locale" content="en_US">
<meta property="og:type" content="article">
<meta property="og:title" content="AWS EC2 Instance Creation Using Ansible Playbook Automation">
<meta property="og:description" content="AWS EC2 Instance Creation Using Ansible Playbook Automation. Provisioning EC2 instance fron ansible master node using boto &amp; boto3 AWS. Git Clone and use it">
<meta property="og:url" content="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/">
<meta property="og:site_name" content="ARKIT">
<meta property="article:publisher" content="https://www.facebook.com/Linuxarkit/">
<meta property="article:author" content="https://www.facebook.com/Linuxarkit">
<meta property="article:tag" content="Ansible Playbooks">
<meta property="article:tag" content="AWS Tutorial">
<meta property="article:section" content="ansible">
<meta property="article:published_time" content="2019-01-04T11:19:55+00:00">
<meta property="og:image" content="https://arkit.co.in/wp-content/uploads/2019/01/AWS-EC2-Instance-Creation-Using-Ansible-Playbook.jpg">
<meta property="og:image:secure_url" content="https://arkit.co.in/wp-content/uploads/2019/01/AWS-EC2-Instance-Creation-Using-Ansible-Playbook.jpg">
<meta property="og:image:width" content="742">
<meta property="og:image:height" content="345">
<meta property="og:image:alt" content="AWS EC2 Instance Creation Using Ansible Playbook">
<meta name="twitter:card" content="summary">
<meta name="twitter:description" content="AWS EC2 Instance Creation Using Ansible Playbook Automation. Provisioning EC2 instance fron ansible master node using boto &amp; boto3 AWS. Git Clone and use it">
<meta name="twitter:title" content="AWS EC2 Instance Creation Using Ansible Playbook Automation">
<meta name="twitter:site" content="@aravikumar48">
<meta name="twitter:image" content="https://arkit.co.in/wp-content/uploads/2019/01/AWS-EC2-Instance-Creation-Using-Ansible-Playbook.jpg">
<meta name="twitter:creator" content="@aravikumar48">
<link rel="dns-prefetch" href="https://s.w.org/">
<link rel="alternate" type="application/rss+xml" title="ARKIT » Feed" href="https://arkit.co.in/feed/">
<link rel="alternate" type="application/rss+xml" title="ARKIT » Comments Feed" href="https://arkit.co.in/comments/feed/">
<link rel="alternate" type="application/rss+xml" title="ARKIT » AWS EC2 Instance Creation Using Ansible Playbook Automation Comments Feed" href="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/feed/">
<link rel="stylesheet" type="text/css" href="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/a7ogu.css" media="all">
<style id="hueman-main-style-inline-css">body{font-family:'Source Sans Pro', Arial, sans-serif;font-size:1.00rem}
@media only screen and (min-width: 720px) {
.nav > li{font-size:1.00rem;}
}.sidebar .widget{padding-left:20px;padding-right:20px;padding-top:20px;}::selection{background-color:#679dbc;}::-moz-selection{background-color:#679dbc;}
a,a+span.hu-external::after,.themeform label .required,#flexslider-featured .flex-direction-nav .flex-next:hover,#flexslider-featured .flex-direction-nav .flex-prev:hover,.post-hover:hover .post-title a,.post-title a:hover,.sidebar.s1 .post-nav li a:hover i,.content .post-nav li a:hover i,.post-related a:hover,.sidebar.s1 .widget_rss ul li a,#footer .widget_rss ul li a,.sidebar.s1 .widget_calendar a,#footer .widget_calendar a,.sidebar.s1 .alx-tab .tab-item-category a,.sidebar.s1 .alx-posts .post-item-category a,.sidebar.s1 .alx-tab li:hover .tab-item-title a,.sidebar.s1 .alx-tab li:hover .tab-item-comment a,.sidebar.s1 .alx-posts li:hover .post-item-title a,#footer .alx-tab .tab-item-category a,#footer .alx-posts .post-item-category a,#footer .alx-tab li:hover .tab-item-title a,#footer .alx-tab li:hover .tab-item-comment a,#footer .alx-posts li:hover .post-item-title a,.comment-tabs li.active a,.comment-awaiting-moderation,.child-menu a:hover,.child-menu .current_page_item > a,.wp-pagenavi a{color:#679dbc;}
.themeform input[type="submit"],.themeform button[type="submit"],.sidebar.s1 .sidebar-top,.sidebar.s1 .sidebar-toggle,#flexslider-featured .flex-control-nav li a.flex-active,.post-tags a:hover,.sidebar.s1 .widget_calendar caption,#footer .widget_calendar caption,.author-bio .bio-avatar:after,.commentlist li.bypostauthor > .comment-body:after,.commentlist li.comment-author-admin > .comment-body:after{background-color:#679dbc;}
.post-format .format-container{border-color:#679dbc;}
.sidebar.s1 .alx-tabs-nav li.active a,#footer .alx-tabs-nav li.active a,.comment-tabs li.active a,.wp-pagenavi a:hover,.wp-pagenavi a:active,.wp-pagenavi span.current{border-bottom-color:#679dbc!important;}
.sidebar.s2 .post-nav li a:hover i,
.sidebar.s2 .widget_rss ul li a,
.sidebar.s2 .widget_calendar a,
.sidebar.s2 .alx-tab .tab-item-category a,
.sidebar.s2 .alx-posts .post-item-category a,
.sidebar.s2 .alx-tab li:hover .tab-item-title a,
.sidebar.s2 .alx-tab li:hover .tab-item-comment a,
.sidebar.s2 .alx-posts li:hover .post-item-title a{color:#82b965;}
.sidebar.s2 .sidebar-top,.sidebar.s2 .sidebar-toggle,.post-comments,.jp-play-bar,.jp-volume-bar-value,.sidebar.s2 .widget_calendar caption{background-color:#82b965;}
.sidebar.s2 .alx-tabs-nav li.active a{border-bottom-color:#82b965;}
.post-comments span:before{border-right-color:#82b965;}
.search-expand,
#nav-topbar.nav-container{background-color:#f16334}
@media only screen and (min-width: 720px) {
#nav-topbar .nav ul{background-color:#f16334;}
}.is-scrolled #header .nav-container.desktop-sticky,
.is-scrolled #header .search-expand{background-color:#f16334;background-color:rgba(241,99,52,0.90)}
.is-scrolled .topbar-transparent #nav-topbar.desktop-sticky .nav ul{background-color:#f16334;background-color:rgba(241,99,52,0.95)}
#header{background-color:#825e9b;}
@media only screen and (min-width: 720px) {
#nav-header .nav ul{background-color:#825e9b;}
}
.is-scrolled #header #nav-mobile{background-color:#454e5c;background-color:rgba(69,78,92,0.90)}
#nav-header.nav-container, #main-header-search .search-expand{background-color:#f16334;}
@media only screen and (min-width: 720px) {
#nav-header .nav ul{background-color:#f16334;}
}
#footer-bottom{background-color:#f16334;}
img{-webkit-border-radius:5px;border-radius:5px;}
body{background-color:#f2af98;}</style>
<link rel="stylesheet" type="text/css" href="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/6f1cm.css" media="all">
<link rel="https://api.w.org/" href="https://arkit.co.in/wp-json/">
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://arkit.co.in/xmlrpc.php?rsd">
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://arkit.co.in/wp-includes/wlwmanifest.xml"> 
<meta name="generator" content="WordPress 5.0.3">
<link rel="shortlink" href="https://arkit.co.in/?p=7164">
<link rel="alternate" type="application/json+oembed" href="https://arkit.co.in/wp-json/oembed/1.0/embed?url=https%3A%2F%2Farkit.co.in%2Faws-ec2-instance-creation-using-ansible%2F">
<link rel="alternate" type="text/xml+oembed" href="https://arkit.co.in/wp-json/oembed/1.0/embed?url=https%3A%2F%2Farkit.co.in%2Faws-ec2-instance-creation-using-ansible%2F&amp;format=xml">
<style>.recentcomments a{display:inline !important;padding:0 !important;margin:0 !important;}</style>
<link rel="amphtml" href="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/amp/"><link rel="icon" href="https://arkit.co.in/wp-content/uploads/2015/09/cropped-logo_ark-32x32.png" sizes="32x32">
<link rel="icon" href="https://arkit.co.in/wp-content/uploads/2015/09/cropped-logo_ark-192x192.png" sizes="192x192">
<link rel="apple-touch-icon-precomposed" href="https://arkit.co.in/wp-content/uploads/2015/09/cropped-logo_ark-180x180.png">
<meta name="msapplication-TileImage" content="https://arkit.co.in/wp-content/uploads/2015/09/cropped-logo_ark-270x270.png">
<script src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/cbgapi.loaded_1" async=""></script><script src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/cbgapi.loaded_0" async=""></script><script async="" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/analytics.js"></script><script>(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){ (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o), m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m) })(window,document,'script','https://www.google-analytics.com/analytics.js','ga'); ga('create', 'UA-68141060-1', 'auto'); ga('send', 'pageview');</script>
<style id="wp-custom-css">.after-article-box{background-color:#044B6A;width:100%px;padding:25px;margin-top:30px;margin-bottom:30px;border:3px solid #ef4423;color:#FFFFFF;}
.entry pre{padding:18px 20px;margin:30px 0;border:1px solid #ddd;line-height:19px;white-space:pre-wrap;word-wrap:break-word;overflow-x:auto;overflow-y:hidden;color:white;border-color:#FF5733;border-style:solid;border-width:0px 1px 0px 4px;background-color:#044B6A;font-family:monospace;font-size:14px;}</style>
<style id="wfc-style-body" data-origin="server">body{font-weight:400;font-style:normal;color:#1c1c1c;}</style><style id="wfc-style-post_content" data-origin="server">section.content .entry-inner p, .page section.content .entry p{font-weight:400;font-style:normal;color:#5b5252;font-size:0.88rem;line-height:1.50rem;}
section.content .entry-inner p:hover, .page section.content .entry p:hover{color:#096cc2;}</style><style id="wfc-style-post_lists" data-origin="server">section.content .entry li{color:#5b5252;font-weight:400;font-style:normal;font-size:0.88rem;}
section.content .entry li:hover{color:#096cc2;}</style><style id="wfc-style-single_post_title" data-origin="server">.single .post-inner .post-title{font-weight:400;font-style:normal;color:#0e94c9;font-size:1.00rem;}</style><style id="wfc-style-blockquote" data-origin="server">section.content .entry blockquote p, .format-quote .post-format blockquote{color:#336587;}</style><style id="wfc-style-site_title" data-origin="server">header#header .site-title a{font-weight:400;font-style:normal;}</style><style id="wfc-style-menu_items" data-origin="server">nav#nav-header .nav li a{font-weight:400;font-style:normal;color:#ffffff;}
nav#nav-header .nav li a:hover{color:#23d35e;}</style><style id="wfc-style-top_menu_items" data-origin="server">nav#nav-topbar .nav li a{font-weight:400;font-style:normal;}
nav#nav-topbar .nav li a:hover{color:#2ae05b;}</style><style id="wfc-style-footer_credits" data-origin="server">footer#footer #footer-bottom #copyright, footer#footer #footer-bottom #credit{font-weight:400;font-style:normal;}</style><style id="wfc-style-site_description" data-origin="server">#header p.site-description{font-weight:400;font-style:normal;}</style><style id="wfc-style-post_links" data-origin="server">section.content .entry a, .format-link .post-format p{text-decoration:underline;color:#117bed;}
section.content .entry a:hover, .format-link .post-format p:hover{color:#7ef02d;}</style>            <style id="grids-css">.post-list .grid-item{float:left;}
.cols-1 .grid-item{width:100%;}
.cols-2 .grid-item{width:50%;}
.cols-3 .grid-item{width:33.3%;}
.cols-4 .grid-item{width:25%;}
@media only screen and (max-width: 719px) {
#grid-wrapper .grid-item{width:100%;}
}</style>
<script data-wpfc-render="false">var Wpfcll={s:[],i:function(){Wpfcll.ss();window.addEventListener('load',function(){window.addEventListener("DOMSubtreeModified",function(e){Wpfcll.ss();Wpfcll.ls(false);},false);Wpfcll.ls(true);});window.addEventListener('scroll',function(){Wpfcll.ls(false);});window.addEventListener('resize',function(){Wpfcll.ls(false);});window.addEventListener('click',function(){Wpfcll.ls(false);});},c:function(e,pageload){var w=document.documentElement.clientHeight || body.clientHeight;var n=pageload ? 0:800;var er=e.getBoundingClientRect();var t=0;var p=e.parentNode;var pr=p.getBoundingClientRect();if(er.x==0 && er.y==0){for(var i=0;i < 10;i++){if(p){if(pr.x==0 && pr.y==0){p=p.parentNode;pr=p.getBoundingClientRect();}else{t=pr.top;break;}}};}else{t=er.top;}if(w - t+n > 0){return true;}return false;},r:function(e,pageload){var s=this;var oc,ot;try{if(s.c(e,pageload)){oc=e.getAttribute("data-wpfc-original-src");ot=e.getAttribute("data-wpfc-original-srcset");if(oc || ot){if(oc){e.setAttribute('src',oc);}if(ot){e.setAttribute('srcset',ot);}e.removeAttribute("data-wpfc-original-src");e.removeAttribute("onload");if(e.tagName=="IFRAME"){e.onload=function(){var s=e.getAttribute("src").match(/templates\/youtube\.html\#(.+)/);var y="https://www.youtube.com/embed/";if(s){try{var i=e.contentDocument || e.contentWindow;if(i.location.href=="about:blank"){e.setAttribute('src',y+s[1]);}}catch(err){e.setAttribute('src',y+s[1]);}}}}}}}catch(error){console.log(error);console.log("==>",e);}},ss:function(){var i=Array.prototype.slice.call(document.getElementsByTagName("img"));var f=Array.prototype.slice.call(document.getElementsByTagName("iframe"));this.s=i.concat(f);},ls:function(pageload){var s=this;[].forEach.call(s.s,function(e,index){s.r(e,pageload);});}};document.addEventListener('DOMContentLoaded',function(){wpfci();});function wpfci(){Wpfcll.i();}</script>
<link href="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/css_003.css" rel="stylesheet"><style id="hide-sharre-count" type="text/css">.sharrre-container.no-counter .box .count {display:none;}</style><style></style><style>.gc-bubbleDefault{background-color:transparent !important;text-align:left;padding:0 !important;margin:0 !important;border:0 !important;table-layout:auto !important}.gc-reset{background-color:transparent !important;border:0 !important;padding:0 !important;margin:0 !important;text-align:left}.pls-bubbleTop{border-bottom:1px solid #ccc !important}.pls-topTail,.pls-vertShimLeft,.pls-contentLeft{background-image:url(//ssl.gstatic.com/s2/oz/images/stars/po/bubblev1/border_3.gif) !important}.pls-topTail{background-repeat:repeat-x !important;background-position:bottom !important}.pls-vertShim{background-color:#fff !important;text-align:right}.tbl-grey .pls-vertShim{background-color:#f5f5f5 !important}.pls-vertShimLeft{background-repeat:repeat-y !important;background-position:right !important;height:4px}.pls-vertShimRight{height:4px}.pls-confirm-container .pls-vertShim{background-color:#fff3c2 !important}.pls-contentWrap{background-color:#fff !important;position:relative !important;vertical-align:top}.pls-contentLeft{background-repeat:repeat-y;background-position:right;vertical-align:top}.pls-dropRight{background-image:url(//ssl.gstatic.com/s2/oz/images/stars/po/bubblev1/bubbleDropR_3.png) !important;background-repeat:repeat-y !important;vertical-align:top}.pls-vert,.pls-tailleft,.pls-dropTR .pls-dropBR,.pls-dropBL,.pls-vert img{vertical-align:top}.pls-dropBottom{background-image:url(//ssl.gstatic.com/s2/oz/images/stars/po/bubblev1/bubbleDropB_3.png) !important;background-repeat:repeat-x !important;width:100%;vertical-align:top}.pls-topLeft{background:inherit !important;text-align:right;vertical-align:bottom}.pls-topRight{background:inherit !important;text-align:left;vertical-align:bottom}.pls-bottomLeft{background:inherit !important;text-align:right}.pls-bottomRight{background:inherit !important;text-align:left;vertical-align:top}.pls-tailtop,.pls-tailright,.pls-tailbottom,.pls-tailleft{display:none;position:relative}.pls-tailbottom,.pls-tailtop,.pls-tailright,.pls-tailleft,.pls-dropTR,.pls-dropBR,.pls-dropBL{background-image:url(//ssl.gstatic.com/s2/oz/images/stars/po/bubblev1/bubbleSprite_3.png) !important;background-repeat:no-repeat}.tbl-grey .pls-tailbottom,.tbl-grey .pls-tailtop,.tbl-grey .pls-tailright,.tbl-grey .pls-tailleft,.tbl-grey .pls-dropTR,.tbl-grey .pls-dropBR,.tbl-grey .pls-dropBL{background-image:url(//ssl.gstatic.com/s2/oz/images/stars/po/bubblev1/bubbleSprite-grey.png) !important}.pls-tailbottom{background-position:-23px 0}.pls-confirm-container .pls-tailbottom{background-position:-23px -10px}.pls-tailtop{background-position:-19px -20px}.pls-tailright{background-position:0 0}.pls-tailleft{background-position:-10px 0}.pls-tailtop{vertical-align:top}.gc-bubbleDefault td{line-height:0;font-size:0}.pls-topLeft img,.pls-topRight img,.pls-tailbottom{vertical-align:bottom}.pls-bottomLeft img,.bubbleDropTR,.pls-dropBottomL img,.pls-dropBottom img,.pls-dropBottomR img,.pls-bottomLeft{vertical-align:top}.pls-dropTR{background-position:0 -22px}.pls-dropBR{background-position:0 -27px}.pls-dropBL{background-position:0 -16px}.pls-spacertop,.pls-spacerright,.pls-spacerbottom,.pls-spacerleft{position:static !important}.pls-spinner{bottom:0;position:absolute;left:0;margin:auto;right:0;top:0} </style></head><span id="warning-container"><i data-reactroot=""></i></span>
<body class="post-template-default single single-post postid-7164 single-format-standard wp-embed-responsive col-2cl full-width topbar-enabled mobile-sidebar-hide-s2 header-desktop-sticky header-mobile-sticky unknown mozilla is-scrolled">
<div id="wrapper"> <header id="header" class="top-menu-mobile-on one-mobile-menu top_menu header-ads-desktop topbar-transparent no-header-img fixed-header-on" style="height: 240px; padding-top: 50px;"> <nav class="nav-container group mobile-menu mobile-sticky" id="nav-mobile" data-menu-id="header-1"> <div class="mobile-title-logo-in-header"> <p class="site-title"><a class="custom-logo-link" href="https://arkit.co.in/" rel="home" title="ARKIT | Home page">ARKIT</a></p></div><div class="ham__navbar-toggler-two collapsed" title="Menu" aria-expanded="false"> <div class="ham__navbar-span-wrapper"> <span class="line line-1"></span> <span class="line line-2"></span> <span class="line line-3"></span></div></div><div class="nav-text"></div><div class="nav-wrap container"> <ul class="nav container-inner group mobile-search"> <li> <form method="get" class="searchform themeform" action="https://arkit.co.in/"> <div> <input type="text" class="search" name="s" onblur="if(this.value=='')this.value='To search type and hit enter';" onfocus="if(this.value=='To search type and hit enter')this.value='';" value="To search type and hit enter"></div></form>                </li>
</ul>
<ul id="menu-mainmenu" class="nav container-inner group"><li id="menu-item-310" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-310"><a href="https://arkit.co.in/home/">Home</a></li>
<li id="menu-item-6740" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6740"><a href="https://arkit.co.in/about-us/">About Us</a></li>
<li id="menu-item-2191" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2191"><a href="http://arkit.co.in/free-books-download-pdf-format/">Free Books</a></li>
<li id="menu-item-6738" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-6738"><a href="https://arkit.co.in/category/netapp-tutorial/">Netapp</a></li>
<li id="menu-item-2190" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2190"><a href="https://feedburner.google.com/fb/a/mailverify?uri=arkit">Subscribe</a></li>
<li id="menu-item-2192" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-2192"><a href="https://arkit.co.in/category/interview-questions-and-answers/">Interview</a></li>
<li id="menu-item-2193" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-2193"><a href="https://arkit.co.in/category/microsoft-sql-dba/">MSSQL</a></li>
<li id="menu-item-2383" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2383"><a href="http://arkit.co.in/become-an-author/">Contribute</a></li>
<li id="menu-item-2478" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2478"><a href="https://www.youtube.com/TechArkit?sub_confirmation=1">Videos</a></li>
<li id="menu-item-6739" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6739"><a href="https://arkit.co.in/linux-online-training-course/">Linux Training</a></li>
</ul></div></nav>  
<nav class="nav-container group desktop-menu desktop-sticky" id="nav-topbar" data-menu-id="header-2" style="max-width: 1349px; transform: translate(0px, -50px);">
<div class="nav-text"></div><div class="topbar-toggle-down"> <i class="fas fa-angle-double-down" aria-hidden="true" data-toggle="down" title="Expand menu"></i> <i class="fas fa-angle-double-up" aria-hidden="true" data-toggle="up" title="Collapse menu"></i></div><div class="nav-wrap container"> <ul id="menu-mainmenu-1" class="nav container-inner group"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-310"><a href="https://arkit.co.in/home/">Home</a></li> <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6740"><a href="https://arkit.co.in/about-us/">About Us</a></li> <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2191"><a href="http://arkit.co.in/free-books-download-pdf-format/">Free Books</a></li> <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-6738"><a href="https://arkit.co.in/category/netapp-tutorial/">Netapp</a></li> <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2190"><a href="https://feedburner.google.com/fb/a/mailverify?uri=arkit">Subscribe</a></li> <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-2192"><a href="https://arkit.co.in/category/interview-questions-and-answers/">Interview</a></li> <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-2193"><a href="https://arkit.co.in/category/microsoft-sql-dba/">MSSQL</a></li> <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2383"><a href="http://arkit.co.in/become-an-author/">Contribute</a></li> <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2478"><a href="https://www.youtube.com/TechArkit?sub_confirmation=1">Videos</a></li> <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6739"><a href="https://arkit.co.in/linux-online-training-course/">Linux Training</a></li> </ul></div><div id="topbar-header-search" class="container"> <div class="container-inner"> <div class="toggle-search"><i class="fas fa-search"></i></div><div class="search-expand"> <div class="search-expand-inner"><form method="get" class="searchform themeform" action="https://arkit.co.in/"> <div> <input type="text" class="search" name="s" onblur="if(this.value=='')this.value='To search type and hit enter';" onfocus="if(this.value=='To search type and hit enter')this.value='';" value="To search type and hit enter"></div></form></div></div></div></div></nav>  
<div class="container group"> <div class="container-inner"> <div class="group pad central-header-zone"> <div class="logo-tagline-group"> <p class="site-title"><a class="custom-logo-link" href="https://arkit.co.in/" rel="home" title="ARKIT | Home page">ARKIT</a></p> <p class="site-description">- Learners Guide.</p></div><div id="header-widgets">
<div id="text-88" class="widget widget_text">			<div class="textwidget"><script async="" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/adsbygoogle.js"></script>
<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-3797659217082577" data-ad-slot="8115781843"></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({});</script></div></div></div></div><nav class="nav-container group desktop-menu" id="nav-header" data-menu-id="header-3">
<div class="nav-text"></div><div class="nav-wrap container"> <ul id="menu-menu2" class="nav container-inner group"><li id="menu-item-475" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-475"><a href="https://arkit.co.in/">Home</a></li> <li id="menu-item-466" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-466"><a href="https://arkit.co.in/about-us/">About Us</a></li> <li id="menu-item-6743" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-6743"><a href="https://arkit.co.in/category/linux/">Linux</a></li> <li id="menu-item-451" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-451"><a href="https://arkit.co.in/category/computer-hardware/">Hardware</a></li> <li id="menu-item-454" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-454"><a href="https://arkit.co.in/category/nagios-solarwinds-op-manager-and-open-nms/">Monitoring Tools</a></li> <li id="menu-item-460" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-460"><a href="https://arkit.co.in/category/all-scripts/">Scripting</a></li> <li id="menu-item-2269" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-2269"><a href="https://arkit.co.in/category/vmware/">VMWare</a></li> <li id="menu-item-452" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-452"><a href="https://arkit.co.in/category/interview-questions-and-answers/">Interview</a></li> <li id="menu-item-6296" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-6296"><a href="https://arkit.co.in/category/automation-tools/">Automation</a></li> <li id="menu-item-6394" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6394"><a href="https://arkit.co.in/support-arkit/">Ask Support</a></li> <li id="menu-item-6744" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6744"><a href="https://arkit.co.in/netapp-course-content/">Netapp Training</a></li> <li id="menu-item-6745" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-6745"><a href="https://arkit.co.in/category/aix-os/">AIX</a></li> <li id="menu-item-6746" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-6746"><a href="https://arkit.co.in/category/networking/">Networking</a></li> </ul></div></nav></div></div></header>
<div class="container" id="page"> <div class="container-inner"> <div class="main" style="overflow: hidden;"> <div class="main-inner group"> <section class="content"> <div class="page-title pad group"> <ul class="meta-single group"> <li class="category"><a href="https://arkit.co.in/category/ansible/" rel="category tag">ansible</a> <span>/</span> <a href="https://arkit.co.in/category/automation-tools/" rel="category tag">Automation Tools</a> <span>/</span> <a href="https://arkit.co.in/category/aws/" rel="category tag">AWS</a></li> <li class="comments"><a href="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/#respond"><i class="far fa-comments"></i>0</a></li> </ul></div><div class="pad group"> <article class="post-7164 post type-post status-publish format-standard has-post-thumbnail hentry category-ansible category-automation-tools category-aws tag-ansible-playbooks tag-aws-tutorial"> <div class="post-inner group"> <h1 class="post-title entry-title fittexted_for_single_post_title" style="font-size: 41.92px;">AWS EC2 Instance Creation Using Ansible Playbook Automation</h1> <p class="post-byline">by <span class="vcard author"> <span class="fn"><a href="https://arkit.co.in/author/admin/" title="Posts by ARK" rel="author">ARK</a></span> </span> · <time class="published" datetime="January 4, 2019">January 4, 2019</time> </p> <div class="clear"></div><div class="entry themeform share fittexted_for_entry" style="font-size: 18px;">
<div class="entry-inner">
<p><span style="font-size: 14pt;">Amazon Web Services is introduced term
 called “Infrastructure as a Code” where you no need to provisioning and
 maintenance manually everything is going to be peace of code. In this 
case Ansible AWS EC2 Instance creation using ansible playbook which 
provides automated provisioning of EC2 instances.</span></p>
<p><span style="font-size: 14pt;">No need of manual login to AWS EC2 
console and clicking and creating instances, use feature to 
provision/create ansible is the power full tool.</span></p><script async="" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/adsbygoogle.js"></script>
<ins class="adsbygoogle" style="display:block; text-align:center;" data-ad-layout="in-article" data-ad-format="fluid" data-ad-client="ca-pub-3797659217082577" data-ad-slot="1547324779"></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({});</script>
<h1 style="font-size: 42.75px;" class="fittexted_for_content_h1"><span style="color: #800080;">AWS EC2 Instance Creation Using Ansible</span></h1>
<p><strong><span style="font-size: 14pt;">Preparing Environment before invoking playbook</span></strong></p>
<p><span style="font-size: 14pt;">I am using Centos 7.4 Operating System
 version as Ansible main node. To communicate with AWS we are going to 
use boto / boto3 aws.</span></p>
<pre># yum install python python-setuptools* ansible git curl wget
# curl -O https://bootstrap.pypa.io/get-pip.py
# python get-pip.py 

$ python --version
Python 2.7.5

$ pip --version
pip 18.1 from /usr/lib/python2.7/site-packages/pip (python 2.7)

# pip install boto 
# pip install boto3</pre>
<p><span style="font-size: 14pt;">Use this <a href="https://arkit.co.in/wp-content/uploads/2018/12/AWS-lab-practice-guide-by-www.server-computer-13-12-2018.pdf" target="_blank" rel="noopener">Amazon lab practice guide</a> to create IAM user with programmatic access and user should have access to create/launch EC2 instance</span></p>
<p><span style="font-size: 14pt;">Create a boto file with access key and access secret id to authenticate to aws</span></p>
<pre># vi ~/.boto

[Credentials]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY</pre>
<h2 style="font-size: 38.25px;" class="fittexted_for_content_h2"><span style="color: #800080;">Write Ansible Playbook to launch aws ec2 instance</span></h2>
<ol>
<li><span style="font-size: 14pt;">Define Variables</span></li>
<li><span style="font-size: 14pt;">Tasks</span> <ol> <li><span style="font-size: 14pt;">Create New Security Group</span></li>
<li><span style="font-size: 14pt;">Launch EC2 Instance </span></li>
<li><span style="font-size: 14pt;">Add Tags for identification</span></li>
</ol>
</li>
</ol>
<pre># git clone https://github.com/techtutorials/ansible-palybooks.git# cd ansible-playbooks</pre>
<p><span style="font-size: 14pt;">Look for spinawsec2.yml file</span></p>
<pre>---
  - name: Provision an EC2 Instance
    hosts: localhost
    connection: local
    gather_facts: False
    tags: provisioning

    vars:
      instance_type: t2.micro
      security_group: webservers
      image: ami-0080e4c5bc078760e
      region: us-east-1
      keypair: sshkeypair
      count: 1

    tasks:

      - name: Create New security group with below given name
        local_action:
          module: ec2_group
          name: "{{ security_group }}"
          description: Security Group for Newly Created EC2 Instance
          region: "{{ region }}"
          rules:
            - proto: tcp
              from_port: 22
              to_port: 22
              cidr_ip: 0.0.0.0/0
            - proto: tcp
              from_port: 80
              to_port: 80
              cidr_ip: 0.0.0.0/0
          rules_egress:
            - proto: all
              cidr_ip: 0.0.0.0/0


      - name: Launch the new t2 micro EC2 Instance
        local_action: ec2
                      group={{ security_group }}
                      instance_type={{ instance_type}}
                      image={{ image }}
                      wait=true
                      region={{ region }}
                      keypair={{ keypair }}
                      count={{count}}
        register: ec2

      - name: Wait for EC2 Instance to Spin-up and ready for SSH access
        local_action: wait_for
                      host={{ item.public_ip }}
                      port=22
                      state=started
        with_items: "{{ ec2.instances }}"

      - name: Adding Tags to Identify
        local_action: ec2_tag resource={{ item.id }} region={{ region }} state=present
        with_items: "{{ ec2.instances }}"
        args:
          tags:
            Name: Web Server
            Owner: Ravi Kumar
            PurPose: Testing EC2 Instance From Ansible

</pre>
<h2 style="font-size: 38.25px;" class="fittexted_for_content_h2"><span style="color: #800080;">Pro’s and Con’s</span></h2>
<p><span style="font-size: 14pt;">Using this ansible playbook aws ec2 
instance creation can be done, however every time when you want to 
launch remember to change below variable values</span></p>
<ul>
<li><span style="font-size: 14pt;">AMI ID</span></li>
<li><span style="font-size: 14pt;">Region </span></li>
<li><span style="font-size: 14pt;">Instance Type</span></li>
<li><span style="font-size: 14pt;">Security Group Name</span></li>
<li><span style="font-size: 14pt;">SSH Key Pair Name</span></li>
<li><span style="font-size: 14pt;">Count of instances to be created</span></li>
</ul>
<p><span style="font-size: 14pt;">To make play book more flexible and interactive delete vars section and pass the same variables on playbook execution</span></p>
<pre><del>    vars:
      instance_type: t2.micro
      security_group: webservers
      image: ami-0080e4c5bc078760e
      region: us-east-1
      keypair: NVirginia
      count: 1</del></pre>
<p><span style="font-size: 14pt;">Example of passing variables while running ansible playbook</span></p>
<pre>ansible-playbook <span class="css-truncate css-truncate-target"><a id="d5c10200ce66ac17d6eafd344f1a9e91-c09dda405e550b66e8ba8dc02b1cd54f2f7e789c" class="js-navigation-open" title="spinawsec2.yml" href="https://github.com/techtutorials/ansible-palybooks/blob/master/spinawsec2.yml">spinawsec2.yml</a></span> -e instance_type=t2.micro -e security_group=WebServers -e image=ami-0080e4c5bc078760e -e region=us-east-1 -e keypair=NVirginia -e count=1</pre>
<p><span style="font-size: 14pt;">That’s about aws ec2 instance creation using ansible playbook.</span></p>
<h2 style="font-size: 38.25px;" class="fittexted_for_content_h2"><span style="color: #800080;">Related Articles</span></h2>
<p><span style="font-size: 14pt;"><a href="https://arkit.co.in/first-configuration-ansible/" target="_blank" rel="noopener">First Configuration After Ansible Installation</a></span></p>
<p><span style="font-size: 14pt;"><a href="https://arkit.co.in/installing-ansible-python-virtual-environment/" target="_blank" rel="noopener">Installing Python virtual Ansible Environment</a></span></p>
<p><span style="font-size: 14pt;"><a href="https://arkit.co.in/write-ansible-playbook-first-time-guide/" target="_blank" rel="noopener">How To Write Ansible Playbook</a></span></p>
<p><span style="font-size: 14pt;"><a href="https://arkit.co.in/configure-snmp-using-ansible-playbook/" target="_blank" rel="noopener">Configure SNMP Using Ansible Playbook</a></span></p>
<p><span style="font-size: 14pt;"><a href="https://arkit.co.in/ansible-playbook-copying-ssh-keys/" target="_blank" rel="noopener">Copying SSH Keys Using Ansible</a></span></p>
<p><span style="font-size: 14pt;"><a href="https://arkit.co.in/install-ansible-tower-rhel-7/" target="_blank" rel="noopener">Install Ansible tower</a></span></p>
<p><span style="font-size: 14pt;"><a href="https://arkit.co.in/access-inbuilt-help-ansible-using-ansible-doc/" target="_blank" rel="noopener">Ansible-Doc Accessing Documentation</a></span></p>
<p><a href="https://arkit.co.in/howto-setup-ansible-practice-lab-using-docker/" target="_blank" rel="noopener"><span style="font-size: 14pt;">Lab Setup Using Docker Containers</span></a></p>
<p class="wpsai_spacing_before_adsense"></p><script async="" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/adsbygoogle.js"></script> <script>(adsbygoogle=window.adsbygoogle||[]).push({ google_ad_client: "ca-pub-3797659217082577", enable_page_level_ads: true });</script><div class="after-article-box">
<p style="text-align: center;"><strong style="color: #FFFFFF; font-size: 20px;">Thanks for your wonderful Support and Encouragement </strong></p>
<h4 style="color: rgb(255, 255, 255); font-size: 27px;" class="fittexted_for_content_h4">Stay Connected with us. Learn More and Earn More</h4>
<ul>
<li style="color: #FFFFFF; font-size: 20px;">Do Not Miss Interesting and Important Articles: <strong><a title="Signin with your Email Address" href="https://feedburner.google.com/fb/a/mailverify?uri=arkit" target="_blank" rel="nofollow">Signin Now</a></strong></li>
<li style="color: #FFFFFF; font-size: 20px;">Download free PDF Books : <a href="http://arkit-in.tradepub.com/category/information-technology/" target="_blank"><strong>Download Anything and Everything for Free</strong></a></li>
<li style="color: #FFFFFF; font-size: 20px;">Stay Connected with Us: <a href="https://www.facebook.com/Linuxarkit/" target="_blank"><strong>Facebook Page</strong></a> | <a href="https://twitter.com/aravikumar48" target="_blank"><strong>Twitt</strong></a> | <strong><a href="https://plus.google.com/+RedhatEnterpriseLinuxStepbyStepGuide/" target="_blank">Google Plus</a> </strong>|<strong> <a href="https://www.linkedin.com/in/ravi-kumar-94530121/" target="_blank">LinkedIn</a> </strong>|<strong> <a href="http://feeds.feedburner.com/arkit" target="_blank">RSS feeds</a></strong></li>
<li style="color: #FFFFFF; font-size: 20px;">High Qualitfy Video Tutorials : <a href="https://www.youtube.com/Techarkit" target="_blank"><strong>All Videos</strong></a></li>
</ul></div><nav class="pagination group">
<div class="wp-pagenavi" role="navigation"> <span class="pages">Page 1 of 1</span><span aria-current="page" class="current">1</span></div></nav></div><div class="sharrre-container" style="position: fixed; top: 100px; left: 889px;"> <span>Share</span> <div id="twitter" data-url="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/" data-text="AWS EC2 Instance Creation Using Ansible Playbook Automation" data-title="Tweet" class="sharrre"><a class="box" href="#"><div class="count" href="#">0</div><div class="share"><i class="fab fa-twitter"></i></div></a></div><div id="facebook" data-url="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/" data-text="AWS EC2 Instance Creation Using Ansible Playbook Automation" data-title="Like" class="sharrre"></div><div id="googleplus" data-url="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/" data-text="AWS EC2 Instance Creation Using Ansible Playbook Automation" data-title="+1" class="sharrre"><a class="box" href="#"><div class="count" href="#">0</div><div class="share"><i class="fab fa-google-plus-square"></i></div></a></div><div id="pinterest" data-url="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/" data-text="AWS EC2 Instance Creation Using Ansible Playbook Automation" data-title="Pin It" class="sharrre"><a class="box" href="#" rel="nofollow"><div class="count" href="#">0</div><div class="share"><i class="fab fa-pinterest"></i></div></a></div><div id="linkedin" data-url="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/" data-text="AWS EC2 Instance Creation Using Ansible Playbook Automation" data-title="Publish on Linked In" class="sharrre"></div></div><style></style>
<div class="clear"></div></div></div></article>
<div class="clear"></div><p class="post-tags"><span>Tags:</span> <a href="https://arkit.co.in/tag/ansible-playbooks/" rel="tag">Ansible Playbooks</a><a href="https://arkit.co.in/tag/aws-tutorial/" rel="tag">AWS Tutorial</a></p>
<div class="author-bio"> <div class="bio-avatar"><img alt="" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/1ca2a02f957e166004ed874ad5b17063.jpg" srcset="https://secure.gravatar.com/avatar/1ca2a02f957e166004ed874ad5b17063?s=256&amp;d=mm&amp;r=g 2x" class="avatar avatar-128 photo" width="128" height="128"></div><p class="bio-name">ARK</p>
<p class="bio-desc">My Name is ARK. Expert in grasping any new technology, Interested in Sharing the knowledge. Learn more &amp; Earn More<a href="https://arkit.co.in/author/ankamahitha/" rel="author">View all Posts</a></p>
<div class="clear"></div></div><ul class="post-nav group">
<li class="next"><a href="https://arkit.co.in/aws-ec2-create-remove-keypair-using-ansible/" rel="next"><i class="fas fa-chevron-right"></i><strong>Next story</strong> <span>AWS EC2 Create &amp; Remove Keypair Using Ansible Playbook</span></a></li>
<li class="previous"><a href="https://arkit.co.in/basic-linux-commands/" rel="prev"><i class="fas fa-chevron-left"></i><strong>Previous story</strong> <span>Basic Linux Commands For Absolute Beginners</span></a></li>
</ul>
<div id="pro-related-posts-wrapper"><div class="czr-css-loader czr-mr-loader dark"><div></div><div></div><div></div></div></div><section id="comments" class="themeform">
<div id="respond" class="comment-respond">
<h3 id="reply-title" class="comment-reply-title">Leave a Reply <small><a rel="nofollow" id="cancel-comment-reply-link" href="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/#respond" style="display:none;">Cancel reply</a></small></h3>			<form action="https://arkit.co.in/wp-comments-post.php" method="post" id="commentform" class="comment-form">
<p class="comment-notes"><span id="email-notes">Your email address will not be published.</span> Required fields are marked <span class="required">*</span></p><p class="comment-form-comment"><label for="comment">Comment</label> <textarea id="comment" name="comment" cols="45" rows="8" maxlength="65525" required="required"></textarea></p><p class="comment-form-author"><label for="author">Name <span class="required">*</span></label> <input id="author" name="author" type="text" size="30" maxlength="245" required="required"></p>
<p class="comment-form-email"><label for="email">Email <span class="required">*</span></label> <input id="email" name="email" type="text" size="30" maxlength="100" aria-describedby="email-notes" required="required"></p>
<p class="comment-form-url"><label for="url">Website</label> <input id="url" name="url" type="text" size="30" maxlength="200"></p>
<p class="form-submit"><input name="submit" type="submit" id="submit" class="submit" value="Post Comment"> <input type="hidden" name="comment_post_ID" value="7164" id="comment_post_ID">
<input type="hidden" name="comment_parent" id="comment_parent" value="0">
</p><p style="display: none;"><input type="hidden" id="akismet_comment_nonce" name="akismet_comment_nonce" value="fc8e2e1058"></p><p style="display: none;"></p>			<input type="hidden" id="ak_js" name="ak_js" value="1556471897821"></form></div></section></div></section>
<div class="sidebar s1 collapsed sticky" data-position="right" data-layout="col-2cl" data-sb-id="s1" style="transform: translateZ(0px); position: fixed; top: 0px; left: 989px;"> <a class="sidebar-toggle" title="Expand Sidebar" style="transform: translate(0px, 0px);"><i class="fas icon-sidebar-toggle"></i></a> <div class="sidebar-content" style="transform: translate(0px, 0px);"> <div class="sidebar-top group"> <p>Follow:</p> <ul class="social-links"><li><a rel="nofollow" class="social-tooltip" title="Follow us on Rss" aria-label="Follow us on Rss" href="https://feedburner.google.com/fb/a/mailverify?uri=arkit" target="_blank" style="color:#e1f44b"><i class="fas fa-rss"></i></a></li><li><a rel="nofollow" class="social-tooltip" title="Follow us on Linkedin" aria-label="Follow us on Linkedin" href="https://in.linkedin.com/in/ravi-kumar-94530121" target="_blank" style="color:#692bc6"><i class="fab fa-linkedin"></i></a></li><li><a rel="nofollow" class="social-tooltip" title="Follow us on Facebook" aria-label="Follow us on Facebook" href="https://www.facebook.com/Linuxarkit/" target="_blank" style="color:#0322a0"><i class="fab fa-facebook"></i></a></li><li><a rel="nofollow" class="social-tooltip" title="Follow us on Google-plus" aria-label="Follow us on Google-plus" href="https://plus.google.com/u/0/+RedhatEnterpriseLinuxStepbyStepGuide/posts" target="_blank" style="color:#dd3333"><i class="fab fa-google-plus"></i></a></li><li><a rel="nofollow" class="social-tooltip" title="Follow us on Twitter" aria-label="Follow us on Twitter" href="https://twitter.com/aravikumar48" target="_blank" style="color:#23edcb"><i class="fab fa-twitter"></i></a></li><li><a rel="nofollow" class="social-tooltip" title="Follow us on Youtube" aria-label="Follow us on Youtube" href="https://www.youtube.com/Techarkit?sub_confirmation=1" target="_blank" style="color:#dd3333"><i class="fab fa-youtube"></i></a></li></ul></div><div id="custom_html-7" class="widget_text widget widget_custom_html"><div class="textwidget custom-html-widget"><script async="" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/adsbygoogle.js"></script>
<ins class="adsbygoogle" style="display:inline-block;width:300px;height:600px" data-ad-client="ca-pub-3797659217082577" data-ad-slot="5751607842"></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({});</script></div></div><div id="custom_html-17" class="widget_text widget widget_custom_html"><h3 class="widget-title">Youtube videos</h3><div class="textwidget custom-html-widget"> <div style="text-indent: 0px; margin: 0px; padding: 0px; background: transparent none repeat scroll 0% 0%; border-style: none; float: none; line-height: normal; font-size: 1px; vertical-align: baseline; display: inline-block; width: 169px; height: 48px;" id="___ytsubscribe_0"><iframe ng-non-bindable="" hspace="0" marginheight="0" marginwidth="0" scrolling="no" style="position: static; top: 0px; width: 169px; margin: 0px; border-style: none; left: 0px; visibility: visible; height: 48px;" tabindex="0" vspace="0" id="I0_1556471897741" name="I0_1556471897741" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/subscribe_embed.htm" data-gapiattached="true" width="100%" frameborder="0"></iframe></div></div></div><div id="alxtabs-5" class="widget widget_hu_tabs"> <h3 class="widget-title">Latest Updates</h3><ul class="alx-tabs-nav group tab-count-4"><li class="alx-tab tab-recent active"><a href="#tab-recent-5" title="Recent Posts"><i class="far fa-clock"></i><span>Recent Posts</span></a></li><li class="alx-tab tab-popular"><a href="#tab-popular-5" title="Popular Posts"><i class="fas fa-star"></i><span>Popular Posts</span></a></li><li class="alx-tab tab-comments"><a href="#tab-comments-5" title="Recent Comments"><i class="far fa-comments"></i><span>Recent Comments</span></a></li><li class="alx-tab tab-tags"><a href="#tab-tags-5" title="Tags"><i class="fas fa-tags"></i><span>Tags</span></a></li></ul> <div class="alx-tabs-container"> <ul id="tab-recent-5" class="alx-tab group thumbs-enabled" style="display: block;"> <li> <div class="tab-item-thumbnail"> <a href="https://arkit.co.in/monitoring-website-url-status/" title="Permalink to Monitoring Website URL Status Using Nagios check_http" class=""> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/Monitoring-website-160x160.jpg" class="attachment-thumb-small size-thumb-small wp-post-image tc-smart-load-skip tc-smart-loaded" alt="Monitoring Website URL Status Using Nagios check_http" style="display: block;" sizes="(max-width: 160px) 100vw, 160px" srcset="https://arkit.co.in/wp-content/uploads/2019/01/Monitoring-website-160x160.jpg 160w, https://arkit.co.in/wp-content/uploads/2019/01/Monitoring-website-150x150.jpg 150w, https://arkit.co.in/wp-content/uploads/2019/01/Monitoring-website-320x320.jpg 320w" width="160" height="160"> </a></div><div class="tab-item-inner group"> <p class="tab-item-category"><a href="https://arkit.co.in/category/nagios/" rel="category tag">Nagios</a></p> <p class="tab-item-title"><a href="https://arkit.co.in/monitoring-website-url-status/" rel="bookmark" title="Permalink to Monitoring Website URL Status Using Nagios check_http">Monitoring Website URL Status Using Nagios check_http</a></p> <p class="tab-item-date">4 Feb, 2019</p></div></li>
<li> <div class="tab-item-thumbnail"> <a href="https://arkit.co.in/aws-ec2-create-remove-keypair-using-ansible/" title="Permalink to AWS EC2 Create &amp; Remove Keypair Using Ansible Playbook" class=""> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/AWS-EC2-Create-and-Remove-Keypair-using-ansible-playbook-160.jpg" class="attachment-thumb-small size-thumb-small wp-post-image tc-smart-load-skip tc-smart-loaded" alt="AWS EC2 Create &amp; Remove Keypair using ansible playbook" style="display: block;" sizes="(max-width: 160px) 100vw, 160px" srcset="https://arkit.co.in/wp-content/uploads/2019/01/AWS-EC2-Create-and-Remove-Keypair-using-ansible-playbook-160x160.jpg 160w, https://arkit.co.in/wp-content/uploads/2019/01/AWS-EC2-Create-and-Remove-Keypair-using-ansible-playbook-150x150.jpg 150w, https://arkit.co.in/wp-content/uploads/2019/01/AWS-EC2-Create-and-Remove-Keypair-using-ansible-playbook-320x320.jpg 320w" width="160" height="160"> </a></div><div class="tab-item-inner group"> <p class="tab-item-category"><a href="https://arkit.co.in/category/ansible/" rel="category tag">ansible</a> / <a href="https://arkit.co.in/category/automation-tools/" rel="category tag">Automation Tools</a> / <a href="https://arkit.co.in/category/aws/" rel="category tag">AWS</a></p> <p class="tab-item-title"><a href="https://arkit.co.in/aws-ec2-create-remove-keypair-using-ansible/" rel="bookmark" title="Permalink to AWS EC2 Create &amp; Remove Keypair Using Ansible Playbook">AWS EC2 Create &amp; Remove Keypair Using Ansible Playbook</a></p> <p class="tab-item-date">16 Jan, 2019</p></div></li>
<li> <div class="tab-item-thumbnail"> <a href="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/" title="Permalink to AWS EC2 Instance Creation Using Ansible Playbook Automation" class=""> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/AWS-EC2-Instance-Creation-Using-Ansible-Playbook-160x160.jpg" class="attachment-thumb-small size-thumb-small wp-post-image tc-smart-load-skip tc-smart-loaded" alt="AWS EC2 Instance Creation Using Ansible Playbook" style="display: block;" sizes="(max-width: 160px) 100vw, 160px" srcset="https://arkit.co.in/wp-content/uploads/2019/01/AWS-EC2-Instance-Creation-Using-Ansible-Playbook-160x160.jpg 160w, https://arkit.co.in/wp-content/uploads/2019/01/AWS-EC2-Instance-Creation-Using-Ansible-Playbook-150x150.jpg 150w, https://arkit.co.in/wp-content/uploads/2019/01/AWS-EC2-Instance-Creation-Using-Ansible-Playbook-320x320.jpg 320w" width="160" height="160"> </a></div><div class="tab-item-inner group"> <p class="tab-item-category"><a href="https://arkit.co.in/category/ansible/" rel="category tag">ansible</a> / <a href="https://arkit.co.in/category/automation-tools/" rel="category tag">Automation Tools</a> / <a href="https://arkit.co.in/category/aws/" rel="category tag">AWS</a></p> <p class="tab-item-title"><a href="https://arkit.co.in/aws-ec2-instance-creation-using-ansible/" rel="bookmark" title="Permalink to AWS EC2 Instance Creation Using Ansible Playbook Automation">AWS EC2 Instance Creation Using Ansible Playbook Automation</a></p> <p class="tab-item-date">4 Jan, 2019</p></div></li>
<li> <div class="tab-item-thumbnail"> <a href="https://arkit.co.in/basic-linux-commands/" title="Permalink to Basic Linux Commands For Absolute Beginners" class=""> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/Basic-Linux-Commands-160x160.jpg" class="attachment-thumb-small size-thumb-small wp-post-image tc-smart-load-skip tc-smart-loaded" alt="Basic Linux Commands" style="display: block;" sizes="(max-width: 160px) 100vw, 160px" srcset="https://arkit.co.in/wp-content/uploads/2018/12/Basic-Linux-Commands-160x160.jpg 160w, https://arkit.co.in/wp-content/uploads/2018/12/Basic-Linux-Commands-150x150.jpg 150w, https://arkit.co.in/wp-content/uploads/2018/12/Basic-Linux-Commands-320x320.jpg 320w" width="160" height="160"> </a></div><div class="tab-item-inner group"> <p class="tab-item-category"><a href="https://arkit.co.in/category/linux/" rel="category tag">Linux</a></p> <p class="tab-item-title"><a href="https://arkit.co.in/basic-linux-commands/" rel="bookmark" title="Permalink to Basic Linux Commands For Absolute Beginners">Basic Linux Commands For Absolute Beginners</a></p> <p class="tab-item-date">27 Dec, 2018</p></div></li>
<li> <div class="tab-item-thumbnail"> <a href="https://arkit.co.in/aws-lab-practice-guide-pdf/" title="Permalink to AWS Lab Practice Guide PDF Download Absolutely Free" class=""> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/aws-lab-practice-guide-160x160.jpg" class="attachment-thumb-small size-thumb-small wp-post-image tc-smart-load-skip tc-smart-loaded" alt="AWS Lab Practice Guide PDF" style="display: block;" sizes="(max-width: 160px) 100vw, 160px" srcset="https://arkit.co.in/wp-content/uploads/2018/12/aws-lab-practice-guide-160x160.jpg 160w, https://arkit.co.in/wp-content/uploads/2018/12/aws-lab-practice-guide-150x150.jpg 150w, https://arkit.co.in/wp-content/uploads/2018/12/aws-lab-practice-guide-320x320.jpg 320w" width="160" height="160"> </a></div><div class="tab-item-inner group"> <p class="tab-item-category"><a href="https://arkit.co.in/category/aws/" rel="category tag">AWS</a></p> <p class="tab-item-title"><a href="https://arkit.co.in/aws-lab-practice-guide-pdf/" rel="bookmark" title="Permalink to AWS Lab Practice Guide PDF Download Absolutely Free">AWS Lab Practice Guide PDF Download Absolutely Free</a></p> <p class="tab-item-date">15 Dec, 2018</p></div></li>
</ul>
<ul id="tab-popular-5" class="alx-tab group thumbs-enabled" style="display: none;">
<li> <div class="tab-item-thumbnail"> <a href="https://arkit.co.in/rhcsa-certification-book/" title="Permalink to RHCSA Certification – Book Written by Ankam Ravi Kumar" class=""> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/RHCSA-Certification-Guide-160x160.png" class="attachment-thumb-small size-thumb-small wp-post-image tc-smart-load-skip tc-smart-loaded" alt="RHCSA Certification Guide" style="display: block;" sizes="(max-width: 160px) 100vw, 160px" srcset="https://arkit.co.in/wp-content/uploads/2016/05/RHCSA-Certification-Guide-160x160.png 160w, https://arkit.co.in/wp-content/uploads/2016/05/RHCSA-Certification-Guide-150x150.png 150w, https://arkit.co.in/wp-content/uploads/2016/05/RHCSA-Certification-Guide-320x320.png 320w" width="160" height="160"> </a></div><div class="tab-item-inner group"> <p class="tab-item-category"><a href="https://arkit.co.in/category/linux/" rel="category tag">Linux</a> / <a href="https://arkit.co.in/category/redhat-linux/" rel="category tag">Redhat Linux</a> / <a href="https://arkit.co.in/category/rhel56/" rel="category tag">rhel56</a></p> <p class="tab-item-title"><a href="https://arkit.co.in/rhcsa-certification-book/" rel="bookmark" title="Permalink to RHCSA Certification – Book Written by Ankam Ravi Kumar">RHCSA Certification – Book Written by Ankam Ravi Kumar</a></p> <p class="tab-item-date">31 May, 2016</p></div></li>
<li> <div class="tab-item-thumbnail"> <a href="https://arkit.co.in/squid-proxy-server/" title="Permalink to Squid Proxy Server Installation RHEL7" class=""> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/squid-proxy-server-installation.png" class="attachment-thumb-small size-thumb-small wp-post-image tc-smart-load-skip tc-smart-loaded" alt="squid proxy server installation" wpfc-lazyload-disable="true" style="display: block;" sizes="(max-width: 160px) 100vw, 160px" srcset="https://arkit.co.in/wp-content/uploads/2016/04/squid-proxy-server-installation.png 373w, https://arkit.co.in/wp-content/uploads/2016/04/squid-proxy-server-installation-300x169.png 300w" width="160" height="90"> </a></div><div class="tab-item-inner group"> <p class="tab-item-category"><a href="https://arkit.co.in/category/centos/" rel="category tag">Centos</a> / <a href="https://arkit.co.in/category/linux/" rel="category tag">Linux</a> / <a href="https://arkit.co.in/category/redhat-linux/" rel="category tag">Redhat Linux</a> / <a href="https://arkit.co.in/category/rhel56/" rel="category tag">rhel56</a> / <a href="https://arkit.co.in/category/rhel7/" rel="category tag">RHEL7</a></p> <p class="tab-item-title"><a href="https://arkit.co.in/squid-proxy-server/" rel="bookmark" title="Permalink to Squid Proxy Server Installation RHEL7">Squid Proxy Server Installation RHEL7</a></p> <p class="tab-item-date">17 Apr, 2016</p></div></li>
<li> <div class="tab-item-thumbnail"> <a href="https://arkit.co.in/monitor-cpu-utilization-using-shell-script/" title="Permalink to Monitor Your CPU Utilization using Shell Script" class=""> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/Monitor-CPU-Utilization-Shell-Script.png" class="attachment-thumb-small size-thumb-small wp-post-image tc-smart-load-skip tc-smart-loaded" alt="Monitor Your CPU Utilization using Shell Script" wpfc-lazyload-disable="true" style="display: block;" sizes="(max-width: 160px) 100vw, 160px" srcset="https://arkit.co.in/wp-content/uploads/2015/12/Monitor-CPU-Utilization-Shell-Script.png 350w, https://arkit.co.in/wp-content/uploads/2015/12/Monitor-CPU-Utilization-Shell-Script-300x171.png 300w" width="160" height="91"> </a></div><div class="tab-item-inner group"> <p class="tab-item-category"><a href="https://arkit.co.in/category/all-scripts/" rel="category tag">Scripting</a> / <a href="https://arkit.co.in/category/shell-scripting/" rel="category tag">shell scripting</a></p> <p class="tab-item-title"><a href="https://arkit.co.in/monitor-cpu-utilization-using-shell-script/" rel="bookmark" title="Permalink to Monitor Your CPU Utilization using Shell Script">Monitor Your CPU Utilization using Shell Script</a></p> <p class="tab-item-date">25 Dec, 2015</p></div></li>
<li> <div class="tab-item-thumbnail"> <a href="https://arkit.co.in/installation-and-configuration-ftp/" title="Permalink to Installation and configuration FTP server in RHEL 7" class=""> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/installation-and-configuration-ftp-server-160x160.png" class="attachment-thumb-small size-thumb-small wp-post-image tc-smart-load-skip tc-smart-loaded" alt="" style="display: block;" sizes="(max-width: 160px) 100vw, 160px" srcset="https://arkit.co.in/wp-content/uploads/2016/06/installation-and-configuration-ftp-server-160x160.png 160w, https://arkit.co.in/wp-content/uploads/2016/06/installation-and-configuration-ftp-server-150x150.png 150w, https://arkit.co.in/wp-content/uploads/2016/06/installation-and-configuration-ftp-server-320x320.png 320w" width="160" height="160"> </a></div><div class="tab-item-inner group"> <p class="tab-item-category"><a href="https://arkit.co.in/category/linux/" rel="category tag">Linux</a> / <a href="https://arkit.co.in/category/rhel7/" rel="category tag">RHEL7</a></p> <p class="tab-item-title"><a href="https://arkit.co.in/installation-and-configuration-ftp/" rel="bookmark" title="Permalink to Installation and configuration FTP server in RHEL 7">Installation and configuration FTP server in RHEL 7</a></p> <p class="tab-item-date">1 Jun, 2016</p></div></li>
<li> <div class="tab-item-thumbnail"> <a href="https://arkit.co.in/35-amazing-server-performance-monitoring-tools/" title="Permalink to 35 Amazing Server Performance Monitoring Tools List You Ever Get" class=""> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/35-Amazing-Server-Performance-Monitoring-Tools-List-You-Ever.png" class="attachment-thumb-small size-thumb-small wp-post-image tc-smart-load-skip tc-smart-loaded" alt="35 Amazing Server Performance Monitoring Tools List You Ever Get" style="display: block;" sizes="(max-width: 160px) 100vw, 160px" srcset="https://arkit.co.in/wp-content/uploads/2016/10/35-Amazing-Server-Performance-Monitoring-Tools-List-You-Ever-Get-160x160.png 160w, https://arkit.co.in/wp-content/uploads/2016/10/35-Amazing-Server-Performance-Monitoring-Tools-List-You-Ever-Get-150x150.png 150w, https://arkit.co.in/wp-content/uploads/2016/10/35-Amazing-Server-Performance-Monitoring-Tools-List-You-Ever-Get-320x320.png 320w" width="160" height="160"> </a></div><div class="tab-item-inner group"> <p class="tab-item-category"><a href="https://arkit.co.in/category/linux/" rel="category tag">Linux</a></p> <p class="tab-item-title"><a href="https://arkit.co.in/35-amazing-server-performance-monitoring-tools/" rel="bookmark" title="Permalink to 35 Amazing Server Performance Monitoring Tools List You Ever Get">35 Amazing Server Performance Monitoring Tools List You Ever Get</a></p> <p class="tab-item-date">29 Oct, 2016</p></div></li>
</ul>
<ul id="tab-comments-5" class="alx-tab group avatars-enabled" style="display: none;">
<li> <div class="tab-item-avatar"> <a href="https://arkit.co.in/setup-linux-lab-yet-home-installing-configuring-ipa-server/#comment-3656"> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/844501e757dd16b9e0aba99a1256648e.jpg" alt="" data-wpfc-original-srcset="https://secure.gravatar.com/avatar/844501e757dd16b9e0aba99a1256648e?s=192&amp;d=mm&amp;r=g 2x" class="avatar avatar-96 photo" srcset="https://secure.gravatar.com/avatar/844501e757dd16b9e0aba99a1256648e?s=192&amp;d=mm&amp;r=g 2x" width="96" height="96"> </a></div><div class="tab-item-inner group"> <div class="tab-item-name">Kudzayi Ndoro says:</div><div class="tab-item-comment"><a href="https://arkit.co.in/setup-linux-lab-yet-home-installing-configuring-ipa-server/#comment-3656">Before klist, do "kinit admin" otherwise you get error: klist:...</a></div></div></li>
<li> <div class="tab-item-avatar"> <a href="https://arkit.co.in/nmcli-command-network-manager-command-line-tool-rhel-7/#comment-3571"> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/f12262edec8cdb158431d8f37f7395ab.jpg" alt="" data-wpfc-original-srcset="https://secure.gravatar.com/avatar/f12262edec8cdb158431d8f37f7395ab?s=192&amp;d=mm&amp;r=g 2x" class="avatar avatar-96 photo" srcset="https://secure.gravatar.com/avatar/f12262edec8cdb158431d8f37f7395ab?s=192&amp;d=mm&amp;r=g 2x" width="96" height="96"> </a></div><div class="tab-item-inner group"> <div class="tab-item-name">zero liquid discharge India says:</div><div class="tab-item-comment"><a href="https://arkit.co.in/nmcli-command-network-manager-command-line-tool-rhel-7/#comment-3571">I like the helpful information you provide to your articles. ...</a></div></div></li>
<li> <div class="tab-item-avatar"> <a href="https://arkit.co.in/amp-validation-wordpress-error-resolution/#comment-3546"> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/83f318e4d939cc5ec2cdd627ce26758f.png" alt="" data-wpfc-original-srcset="https://secure.gravatar.com/avatar/83f318e4d939cc5ec2cdd627ce26758f?s=192&amp;d=mm&amp;r=g 2x" class="avatar avatar-96 photo" srcset="https://secure.gravatar.com/avatar/83f318e4d939cc5ec2cdd627ce26758f?s=192&amp;d=mm&amp;r=g 2x" width="96" height="96"> </a></div><div class="tab-item-inner group"> <div class="tab-item-name">titanium says:</div><div class="tab-item-comment"><a href="https://arkit.co.in/amp-validation-wordpress-error-resolution/#comment-3546">great article. I have the same problem but in the...</a></div></div></li>
<li> <div class="tab-item-avatar"> <a href="https://arkit.co.in/ansible-installation-steps-red-hat-enterprise-linux-7/#comment-3386"> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/0a1748d08894460326cfa71fbaa5ec7b.jpg" alt="" data-wpfc-original-srcset="https://secure.gravatar.com/avatar/0a1748d08894460326cfa71fbaa5ec7b?s=192&amp;d=mm&amp;r=g 2x" class="avatar avatar-96 photo" srcset="https://secure.gravatar.com/avatar/0a1748d08894460326cfa71fbaa5ec7b?s=192&amp;d=mm&amp;r=g 2x" width="96" height="96"> </a></div><div class="tab-item-inner group"> <div class="tab-item-name">arvind says:</div><div class="tab-item-comment"><a href="https://arkit.co.in/ansible-installation-steps-red-hat-enterprise-linux-7/#comment-3386">I've encountered the following error: [root@ansiblemaster tmp]# ansible...</a></div></div></li>
<li> <div class="tab-item-avatar"> <a href="https://arkit.co.in/reviewboard-installation-complete-guide-ubuntu-os/#comment-3310"> <img src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/b9befe41148dbf6b930e79600bc53962.jpg" alt="" data-wpfc-original-srcset="https://secure.gravatar.com/avatar/b9befe41148dbf6b930e79600bc53962?s=192&amp;d=mm&amp;r=g 2x" class="avatar avatar-96 photo" srcset="https://secure.gravatar.com/avatar/b9befe41148dbf6b930e79600bc53962?s=192&amp;d=mm&amp;r=g 2x" width="96" height="96"> </a></div><div class="tab-item-inner group"> <div class="tab-item-name">Shruthi says:</div><div class="tab-item-comment"><a href="https://arkit.co.in/reviewboard-installation-complete-guide-ubuntu-os/#comment-3310">Hi, How to login into admin page? What do I...</a></div></div></li>
</ul>
<ul id="tab-tags-5" class="alx-tab group" style="display: none;">
<li> <a href="https://arkit.co.in/tag/arkit/" class="tag-cloud-link tag-link-392 tag-link-position-1" style="font-size: 22pt;" aria-label="arkit (36 items)">arkit</a> <a href="https://arkit.co.in/tag/awk-scripting/" class="tag-cloud-link tag-link-121 tag-link-position-2" style="font-size: 10.825688073394pt;" aria-label="awk scripting (4 items)">awk scripting</a> <a href="https://arkit.co.in/tag/cloud/" class="tag-cloud-link tag-link-101 tag-link-position-3" style="font-size: 9.5412844036697pt;" aria-label="cloud (3 items)">cloud</a> <a href="https://arkit.co.in/tag/clustered-data-ontap/" class="tag-cloud-link tag-link-189 tag-link-position-4" style="font-size: 11.853211009174pt;" aria-label="clustered data ontap (5 items)">clustered data ontap</a> <a href="https://arkit.co.in/tag/cluster-mode/" class="tag-cloud-link tag-link-28 tag-link-position-5" style="font-size: 9.5412844036697pt;" aria-label="Cluster mode (3 items)">Cluster mode</a> <a href="https://arkit.co.in/tag/c-mode/" class="tag-cloud-link tag-link-65 tag-link-position-6" style="font-size: 11.853211009174pt;" aria-label="C Mode (5 items)">C Mode</a> <a href="https://arkit.co.in/tag/computer-hardware/" class="tag-cloud-link tag-link-22 tag-link-position-7" style="font-size: 14.036697247706pt;" aria-label="Computer Hardware (8 items)">Computer Hardware</a> <a href="https://arkit.co.in/tag/computer-hardware-course/" class="tag-cloud-link tag-link-447 tag-link-position-8" style="font-size: 12.752293577982pt;" aria-label="computer hardware course (6 items)">computer hardware course</a> <a href="https://arkit.co.in/tag/computer-networking/" class="tag-cloud-link tag-link-422 tag-link-position-9" style="font-size: 13.394495412844pt;" aria-label="computer networking (7 items)">computer networking</a> <a href="https://arkit.co.in/tag/computer-networking-course/" class="tag-cloud-link tag-link-706 tag-link-position-10" style="font-size: 9.5412844036697pt;" aria-label="computer Networking course (3 items)">computer Networking course</a> <a href="https://arkit.co.in/tag/emc-san-training/" class="tag-cloud-link tag-link-736 tag-link-position-11" style="font-size: 10.825688073394pt;" aria-label="EMC SAN Training (4 items)">EMC SAN Training</a> <a href="https://arkit.co.in/tag/flash-storage/" class="tag-cloud-link tag-link-156 tag-link-position-12" style="font-size: 8pt;" aria-label="Flash Storage (2 items)">Flash Storage</a> <a href="https://arkit.co.in/tag/introduction-to-linux/" class="tag-cloud-link tag-link-72 tag-link-position-13" style="font-size: 8pt;" aria-label="Introduction to Linux (2 items)">Introduction to Linux</a> <a href="https://arkit.co.in/tag/linux/" class="tag-cloud-link tag-link-123 tag-link-position-14" style="font-size: 12.752293577982pt;" aria-label="linux (6 items)">linux</a> <a href="https://arkit.co.in/tag/linux-tutorial/" class="tag-cloud-link tag-link-476 tag-link-position-15" style="font-size: 14.036697247706pt;" aria-label="Linux tutorial (8 items)">Linux tutorial</a> <a href="https://arkit.co.in/tag/nagios/" class="tag-cloud-link tag-link-149 tag-link-position-16" style="font-size: 10.825688073394pt;" aria-label="Nagios (4 items)">Nagios</a> <a href="https://arkit.co.in/tag/nagios-installation-in-rhel7/" class="tag-cloud-link tag-link-125 tag-link-position-17" style="font-size: 8pt;" aria-label="nagios installation in RHEL7 (2 items)">nagios installation in RHEL7</a> <a href="https://arkit.co.in/tag/nagios-monitoring-tool/" class="tag-cloud-link tag-link-129 tag-link-position-18" style="font-size: 9.5412844036697pt;" aria-label="nagios monitoring tool (3 items)">nagios monitoring tool</a> <a href="https://arkit.co.in/tag/ncsa/" class="tag-cloud-link tag-link-99 tag-link-position-19" style="font-size: 18.532110091743pt;" aria-label="NCSA (19 items)">NCSA</a> <a href="https://arkit.co.in/tag/ncsa-certification/" class="tag-cloud-link tag-link-159 tag-link-position-20" style="font-size: 8pt;" aria-label="NCSA Certification (2 items)">NCSA Certification</a> <a href="https://arkit.co.in/tag/netapp/" class="tag-cloud-link tag-link-94 tag-link-position-21" style="font-size: 21.229357798165pt;" aria-label="Netapp (31 items)">Netapp</a> <a href="https://arkit.co.in/tag/netapp-certified-storage-associate/" class="tag-cloud-link tag-link-158 tag-link-position-22" style="font-size: 11.853211009174pt;" aria-label="Netapp certified Storage Associate (5 items)">Netapp certified Storage Associate</a> <a href="https://arkit.co.in/tag/netapp-cluster-mode/" class="tag-cloud-link tag-link-34 tag-link-position-23" style="font-size: 11.853211009174pt;" aria-label="Netapp Cluster Mode (5 items)">Netapp Cluster Mode</a> <a href="https://arkit.co.in/tag/netapp-commands/" class="tag-cloud-link tag-link-35 tag-link-position-24" style="font-size: 8pt;" aria-label="Netapp Commands (2 items)">Netapp Commands</a> <a href="https://arkit.co.in/tag/netapp-tutorials/" class="tag-cloud-link tag-link-248 tag-link-position-25" style="font-size: 9.5412844036697pt;" aria-label="Netapp tutorials (3 items)">Netapp tutorials</a> <a href="https://arkit.co.in/tag/networking/" class="tag-cloud-link tag-link-374 tag-link-position-26" style="font-size: 11.853211009174pt;" aria-label="networking (5 items)">networking</a> <a href="https://arkit.co.in/tag/nrpe/" class="tag-cloud-link tag-link-179 tag-link-position-27" style="font-size: 8pt;" aria-label="NRPE (2 items)">NRPE</a> <a href="https://arkit.co.in/tag/nsclient/" class="tag-cloud-link tag-link-152 tag-link-position-28" style="font-size: 8pt;" aria-label="NSClient++ (2 items)">NSClient++</a> <a href="https://arkit.co.in/tag/oncommand-system-manager/" class="tag-cloud-link tag-link-184 tag-link-position-29" style="font-size: 8pt;" aria-label="oncommand system manager (2 items)">oncommand system manager</a> <a href="https://arkit.co.in/tag/oncommand-unified-manager/" class="tag-cloud-link tag-link-185 tag-link-position-30" style="font-size: 8pt;" aria-label="oncommand unified manager (2 items)">oncommand unified manager</a> <a href="https://arkit.co.in/tag/pc-hardware/" class="tag-cloud-link tag-link-16 tag-link-position-31" style="font-size: 8pt;" aria-label="PC Hardware (2 items)">PC Hardware</a> <a href="https://arkit.co.in/tag/redhat-linux/" class="tag-cloud-link tag-link-43 tag-link-position-32" style="font-size: 9.5412844036697pt;" aria-label="Redhat Linux (3 items)">Redhat Linux</a> <a href="https://arkit.co.in/tag/redhat-linux-7/" class="tag-cloud-link tag-link-18 tag-link-position-33" style="font-size: 8pt;" aria-label="Redhat Linux 7 (2 items)">Redhat Linux 7</a> <a href="https://arkit.co.in/tag/resistive-ram/" class="tag-cloud-link tag-link-168 tag-link-position-34" style="font-size: 8pt;" aria-label="resistive RAM (2 items)">resistive RAM</a> <a href="https://arkit.co.in/tag/rhce/" class="tag-cloud-link tag-link-474 tag-link-position-35" style="font-size: 12.752293577982pt;" aria-label="RHCE (6 items)">RHCE</a> <a href="https://arkit.co.in/tag/rhcsa/" class="tag-cloud-link tag-link-475 tag-link-position-36" style="font-size: 11.853211009174pt;" aria-label="RHCSA (5 items)">RHCSA</a> <a href="https://arkit.co.in/tag/rhel7/" class="tag-cloud-link tag-link-41 tag-link-position-37" style="font-size: 9.5412844036697pt;" aria-label="RHEL7 (3 items)">RHEL7</a> <a href="https://arkit.co.in/tag/shell-scripting/" class="tag-cloud-link tag-link-364 tag-link-position-38" style="font-size: 11.853211009174pt;" aria-label="shell scripting (5 items)">shell scripting</a> <a href="https://arkit.co.in/tag/storage-virtualization/" class="tag-cloud-link tag-link-105 tag-link-position-39" style="font-size: 8pt;" aria-label="Storage virtualization (2 items)">Storage virtualization</a> <a href="https://arkit.co.in/tag/techtutorial/" class="tag-cloud-link tag-link-442 tag-link-position-40" style="font-size: 20.45871559633pt;" aria-label="techtutorial (27 items)">techtutorial</a> <a href="https://arkit.co.in/tag/tech-tutorial/" class="tag-cloud-link tag-link-441 tag-link-position-41" style="font-size: 20.587155963303pt;" aria-label="tech tutorial (28 items)">tech tutorial</a> <a href="https://arkit.co.in/tag/tech-tutorials/" class="tag-cloud-link tag-link-201 tag-link-position-42" style="font-size: 12.752293577982pt;" aria-label="Tech Tutorials (6 items)">Tech Tutorials</a> <a href="https://arkit.co.in/tag/thegeekstuff/" class="tag-cloud-link tag-link-212 tag-link-position-43" style="font-size: 9.5412844036697pt;" aria-label="thegeekstuff (3 items)">thegeekstuff</a> <a href="https://arkit.co.in/tag/ubuntu-14-04/" class="tag-cloud-link tag-link-32 tag-link-position-44" style="font-size: 8pt;" aria-label="ubuntu 14.04 (2 items)">ubuntu 14.04</a> <a href="https://arkit.co.in/tag/yum/" class="tag-cloud-link tag-link-616 tag-link-position-45" style="font-size: 9.5412844036697pt;" aria-label="YUM (3 items)">YUM</a> </li>
</ul></div></div><div id="custom_html-8" class="widget_text widget widget_custom_html"><div class="textwidget custom-html-widget"><script async="" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/adsbygoogle.js"></script>
<ins class="adsbygoogle" style="display:inline-block;width:300px;height:250px" data-ad-client="ca-pub-3797659217082577" data-ad-slot="4794927043"></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({});</script></div></div><div id="custom_html-9" class="widget_text widget widget_custom_html"><div class="textwidget custom-html-widget"><form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://feedburner.google.com/fb/a/mailverify" method="post" target="popupwindow" onsubmit="window.open('https://feedburner.google.com/fb/a/mailverify?uri=arkit', 'popupwindow', 'scrollbars=yes,width=550,height=520');return true"><p>Enter your email address:</p><p><input type="text" style="width:140px" name="email"></p><input type="hidden" value="arkit" name="uri"><input type="hidden" name="loc" value="en_US"><input type="submit" value="Subscribe"><p><a href="https://feedburner.google.com/" target="_blank"></a></p></form></div></div></div></div></div></div></div></div><footer id="footer">
<section class="container" id="footer-full-width-widget">
<div class="container-inner"> <div id="custom_html-19" class="widget_text widget widget_custom_html"><div class="textwidget custom-html-widget"><a target="_blank" rel="nofollow" href="https://www.youtube.com/Techarkit?sub_confirmation=1"><img onload="Wpfcll.r(this,true);" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/blank.gif" data-wpfc-original-src="https://arkit.co.in/wp-content/uploads/2018/09/red-hat-certification-guide.png"></a></div></div><div id="custom_html-11" class="widget_text widget widget_custom_html"><div class="textwidget custom-html-widget"><script async="" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/adsbygoogle.js"></script>
<ins class="adsbygoogle" style="display:block" data-ad-format="autorelaxed" data-ad-client="ca-pub-3797659217082577" data-ad-slot="7583914248"></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({});</script></div></div></div></section>
<section class="container" id="footer-widgets">
<div class="container-inner"> <div class="pad group"> <div class="footer-widget-1 grid one-fourth"> <div id="custom_html-12" class="widget_text widget widget_custom_html"><h3 class="widget-title">Linux Tutorial/Guides</h3><div class="textwidget custom-html-widget"><ul class="alx-posts group"> <li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/one-linux-tutorial/" rel="bookmark" title="Everything You need to learn for RHCSA and RHCE">Complete Linux Tutorial For Beginners</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/category/all-scripts/" rel="bookmark" title="Shell Scripting Tutorial for Beginners">Shell Scripting Tutorial for Beginners</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/category/nagios/" rel="bookmark" title="Nagios Monitoring Implementation from scratch">Enterprise Monitoring Tool Nagios Implementataion Guide</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/pxe-boot-server-configuration/" rel="bookmark" title="PXE Boot Server installation and configuration steps">PXE Boot Server Installation and Configuration</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/automated-os-installation-using-kickstart-method-linux-rhel7/" rel="bookmark" title="Automated OS Installation">Automated OS installation Kick Start Server</a></p></div></li>
</ul></div></div><div id="text-124" class="widget widget_text">			<div class="textwidget"><script async="" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/adsbygoogle.js"></script>
<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-3797659217082577" data-ad-slot="7583914248" data-ad-format="autorelaxed"></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({});</script></div></div></div><div class="footer-widget-2 grid one-fourth"> <div id="custom_html-13" class="widget_text widget widget_custom_html"><h3 class="widget-title">Servers Installation and Configuration</h3><div class="textwidget custom-html-widget"> <ul class="alx-posts group"> <li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/master-dns-configuration-linux/" rel="bookmark" title="Master DNS Server Installation and Configuration RHEL 7">DNS Server Installation and Configuration RHEL 7</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/dhcp-server-rhel7/" rel="bookmark" title="DHCP Server Installation Step by Step Guide">DHCP Server Installation Step by Step Guide</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/samba-share-multi-user-access/" rel="bookmark" title="Samba Server with Multiple User Access">Samba Server with Multiple User Access</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/web-server-installation/" rel="bookmark" title="Web Server Installation and Configuration">Deploying Web Server</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/iscsi-server-installation-providing-remote-block-storage/" rel="bookmark" title="iSCSI Server installation and configuration">iSCSI Server installation and configuration</a></p></div></li>
</ul></div></div></div><div class="footer-widget-3 grid one-fourth"> <div id="custom_html-14" class="widget_text widget widget_custom_html"><h3 class="widget-title">Useful Scripts</h3><div class="textwidget custom-html-widget"><ul class="alx-posts group"> <li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/monitor-cpu-utilization-using-shell-script/" rel="bookmark" title="Monitor CPU Utilization Using Shell Script">Monitor CPU Utilization Using Shell Script</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/debug-shell-script-easily-identify-errors/" rel="bookmark" title="Troubleshooting Shell script errors">Debugging Shell script errors easy way</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/disk-space-monitoring-script/" rel="bookmark" title="Disk Utilization Monitoring and Get Email Alert">Disk Utilization Monitoring and Get Email Alert</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/generate-nagios-configuration-using-shell-script/" rel="bookmark" title="Generate Nagios configuration in Seconds">Generate Nagios configuration in Seconds</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/convert-time-seconds/" rel="bookmark" title="Convert Seconds into Hours Shell Script">Convert Seconds into Hours Shell Script</a></p></div></li>
</ul></div></div></div><div class="footer-widget-4 grid one-fourth last"> <div id="custom_html-15" class="widget_text widget widget_custom_html"><h3 class="widget-title">Netapp Tutorial/Guides</h3><div class="textwidget custom-html-widget"><ul class="alx-posts group"> <li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/migrate-netapp-cifs-shares/" rel="bookmark" title="How To Migrate CIFS Shares from One volume to Another Volume">How To Migrate CIFS Shares from One volume to Another Volume</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/volume-efficiency-policy-netapp/" rel="bookmark" title="How to Do Data Deduplication in Netapp">How to Do Data Deduplication in Netapp</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/snapdrive-disk-connect-using-script-netapp/" rel="bookmark" title="How To connect Netapp Disk using snapdrive script">How To connect Netapp Disk using snapdrive script</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/ict-inventory-collect-tool-netapp/" rel="bookmark" title="Inventory Collection Tool - ICT Netapp">Inventory Collection Tool - ICT Netapp</a></p></div></li>
<li> <div class="post-item-inner group"> <p class="post-item-title"><a href="https://arkit.co.in/snapmirror-setup-scratch-netapp-cluster/" rel="bookmark" title="Snapmirror Setup from scratch">How To Setup Snapmirror from Scratch Netapp</a></p></div></li>
</ul></div></div></div></div></div></section>
<nav class="nav-container group" id="nav-footer" data-menu-id="footer-4" data-menu-scrollable="false">
<div class="ham__navbar-toggler-two collapsed" title="Menu" aria-expanded="false"> <div class="ham__navbar-span-wrapper"> <span class="line line-1"></span> <span class="line line-2"></span> <span class="line line-3"></span></div></div><div class="nav-text"></div><div class="nav-wrap"> <ul id="menu-menu-1" class="nav container group"><li id="menu-item-3535" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3535"><a href="https://arkit.co.in/cookie-policy/">Cookies</a></li> <li id="menu-item-107" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-107"><a href="https://arkit.co.in/declaration/">Declaimer</a></li> <li id="menu-item-100" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-100"><a href="https://arkit.co.in/category/tips-and-tricks/">Tricks</a></li> <li id="menu-item-2442" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2442"><a href="https://arkit.co.in/downloads/">Free Download</a></li> <li id="menu-item-6741" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6741"><a href="https://arkit.co.in/support-arkit/">Support</a></li> <li id="menu-item-6742" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6742"><a href="https://arkit.co.in/about-founder-of-arkit/">About Founder</a></li> </ul></div></nav>
<section class="container" id="footer-bottom">
<div class="container-inner"> <a id="back-to-top" href="#"><i class="fas fa-angle-up"></i></a> <div class="pad group"> <div class="grid one-half"> <div id="copyright"> <p>All Copyrights Reserved © Tech Tutorials 2008 - 2018 </p><p>This work is licensed under a <a href="http://creativecommons.org/licenses/by-nc/4.0/" rel="license"><b style="color:#ccc">(cc) BY-NC 4.0</b></a></p><p></p></div></div><div class="grid one-half last"> <ul class="social-links"><li><a rel="nofollow" class="social-tooltip" title="Follow us on Rss" aria-label="Follow us on Rss" href="https://feedburner.google.com/fb/a/mailverify?uri=arkit" target="_blank" style="color:#e1f44b"><i class="fas fa-rss"></i></a></li><li><a rel="nofollow" class="social-tooltip" title="Follow us on Linkedin" aria-label="Follow us on Linkedin" href="https://in.linkedin.com/in/ravi-kumar-94530121" target="_blank" style="color:#692bc6"><i class="fab fa-linkedin"></i></a></li><li><a rel="nofollow" class="social-tooltip" title="Follow us on Facebook" aria-label="Follow us on Facebook" href="https://www.facebook.com/Linuxarkit/" target="_blank" style="color:#0322a0"><i class="fab fa-facebook"></i></a></li><li><a rel="nofollow" class="social-tooltip" title="Follow us on Google-plus" aria-label="Follow us on Google-plus" href="https://plus.google.com/u/0/+RedhatEnterpriseLinuxStepbyStepGuide/posts" target="_blank" style="color:#dd3333"><i class="fab fa-google-plus"></i></a></li><li><a rel="nofollow" class="social-tooltip" title="Follow us on Twitter" aria-label="Follow us on Twitter" href="https://twitter.com/aravikumar48" target="_blank" style="color:#23edcb"><i class="fab fa-twitter"></i></a></li><li><a rel="nofollow" class="social-tooltip" title="Follow us on Youtube" aria-label="Follow us on Youtube" href="https://www.youtube.com/Techarkit?sub_confirmation=1" target="_blank" style="color:#dd3333"><i class="fab fa-youtube"></i></a></li></ul></div></div></div></section>
</footer></div><noscript id="wpfc-google-fonts"><link rel="stylesheet" id="tc-front-gfonts" href="//fonts.googleapis.com/css?family=Source+Sans+Pro:regular%7CPoppins:regular%7CRoboto+Condensed:regular">
<link id="hu-user-gfont" href="//fonts.googleapis.com/css?family=Source+Sans+Pro:400,300italic,300,400italic,600&subset=latin,latin-ext" rel="stylesheet" type="text/css">
</noscript>
<script>var WfcFrontParams={"effectsAndIconsSelectorCandidates":[],"wfcOptions":null};</script>
<script>var HUParams={"_disabled":[],"SmoothScroll":{"Enabled":false,"Options":{"touchpadSupport":false}},"centerAllImg":"1","timerOnScrollAllBrowsers":"1","extLinksStyle":"","extLinksTargetExt":"","extLinksSkipSelectors":{"classes":["btn","button"],"ids":[]},"imgSmartLoadEnabled":"1","imgSmartLoadOpts":{"parentSelectors":[".container .content",".container .sidebar","#footer","#header-widgets"],"opts":{"excludeImg":[".tc-holder-img"],"fadeIn_options":100}},"goldenRatio":"1.618","gridGoldenRatioLimit":"350","sbStickyUserSettings":{"desktop":true,"mobile":true},"isWPMobile":"","menuStickyUserSettings":{"desktop":"stick_up","mobile":"stick_up"},"mobileSubmenuExpandOnClick":"","submenuTogglerIcon":"<i class=\"fas fa-angle-down\"><\/i>","isDevMode":"","ajaxUrl":"https:\/\/arkit.co.in\/?huajax=1","frontNonce":{"id":"HuFrontNonce","handle":"2d915d9919"},"userStarted":{"with":"before|1.1.10","on":{"date":"2019-01-16 05:47:47.912208","timezone_type":3,"timezone":"UTC"}},"isWelcomeNoteOn":"","welcomeContent":"","i18n":{"collapsibleExpand":"Expand","collapsibleCollapse":"Collapse"},"fitTextMap":{"single_post_title":{"selectors":".single h1.entry-title","minEm":1.375,"maxEm":2.62000000000000010658141036401502788066864013671875},"page_title":{"selectors":".page-title h1","minEm":1,"maxEm":1.3000000000000000444089209850062616169452667236328125},"home_page_title":{"selectors":".home .page-title","minEm":1,"maxEm":1.1999999999999999555910790149937383830547332763671875,"compression":2.5},"post_titles":{"selectors":".blog .post-title, .archive .post-title","minEm":1.375,"maxEm":1.475000000000000088817841970012523233890533447265625},"featured_post_titles":{"selectors":".featured .post-title","minEm":1.375,"maxEm":2.125},"comments":{"selectors":".commentlist li","minEm":0.8125,"maxEm":0.93000000000000004884981308350688777863979339599609375,"compression":2.5},"entry":{"selectors":".entry","minEm":0.9375,"maxEm":1.125,"compression":2.5},"content_h1":{"selectors":".entry h1, .woocommerce div.product h1.product_title","minEm":1.7578125,"maxEm":2.671875},"content_h2":{"selectors":".entry h2","minEm":1.5234375,"maxEm":2.390625},"content_h3":{"selectors":".entry h3","minEm":1.40625,"maxEm":1.96875},"content_h4":{"selectors":".entry h4","minEm":1.2890625,"maxEm":1.6875},"content_h5":{"selectors":".entry h5","minEm":1.0546875,"maxEm":1.40625},"content_h6":{"selectors":".entry h6","minEm":0.9375,"maxEm":1.265625,"compression":2.5}},"userFontSize":"16","fitTextCompression":"1.5"};</script>
<script>document.documentElement.className=document.documentElement.className.replace("no-js","js");</script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","url":"https://arkit.co.in/","sameAs":["https://www.facebook.com/Linuxarkit/","https://www.linkedin.com/in/ravi-kumar-94530121/","https://www.youtube.com/Techarkit","https://twitter.com/aravikumar48"],"@id":"https://arkit.co.in/#organization","name":"ArkIt Solutions Pvt Ltd","logo":""}</script>
<script src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/6f1cn.js" type="text/javascript"></script>
<!--[if lt IE 9]><script src="//arkit.co.in/wp-content/cache/wpfc-minified/fhnm6538/6f1co.js"></script><![endif]-->
<!--[if lt IE 9]><script src="//arkit.co.in/wp-content/cache/wpfc-minified/13o7yadv/6f1co.js"></script><![endif]-->
<script>jQuery(function($){
$('head').append($('<style>', { id:'hide-sharre-count', type:'text/css', html:'.sharrre-container.no-counter .box .count {display:none;}' }));
$('#twitter').sharrre({
share: {
twitter: true
},
template: '<a class="box" href="#"><div class="count" href="#">{total}</div><div class="share"><i class="fab fa-twitter"></i></div></a>',
enableHover: false,
enableTracking: true,
buttons: { twitter: {via: 'aravikumar48'}},
click: function(api, options){
api.simulateClick();
api.openPopup('twitter');
}});
$('#facebook').sharrre({
share: {
facebook: true
},
template: '<a class="box" href="#"><div class="count" href="#">{total}</div><div class="share"><i class="fab fa-facebook-square"></i></div></a>',
enableHover: false,
enableTracking: true,
buttons:{layout: 'box_count'},
click: function(api, options){
api.simulateClick();
api.openPopup('facebook');
}});
$('#googleplus').sharrre({
share: {
googlePlus: true
},
template: '<a class="box" href="#"><div class="count" href="#">{total}</div><div class="share"><i class="fab fa-google-plus-square"></i></div></a>',
enableHover: false,
enableTracking: true,
buttons:{size: 'tall'},
urlCurl: 'https://arkit.co.in/wp-content/themes/hueman-pro/addons/assets/front/js/sharrre.php',
click: function(api, options){
api.simulateClick();
api.openPopup('googlePlus');
}});
$('#pinterest').sharrre({
share: {
pinterest: true
},
template: '<a class="box" href="#" rel="nofollow"><div class="count" href="#">{total}</div><div class="share"><i class="fab fa-pinterest"></i></div></a>',
enableHover: false,
enableTracking: true,
buttons: {
pinterest: {
description: 'AWS EC2 Instance Creation Using Ansible Playbook Automation',media: 'https://arkit.co.in/wp-content/uploads/2019/01/AWS-EC2-Instance-Creation-Using-Ansible-Playbook.jpg'        				}},
click: function(api, options){
api.simulateClick();
api.openPopup('pinterest');
}});
$('#linkedin').sharrre({
share: {
linkedin: true
},
template: '<a class="box" href="#" rel="nofollow"><div class="count" href="#">{total}</div><div class="share"><i class="fab fa-linkedin"></i></div></a>',
enableHover: false,
enableTracking: true,
buttons: {
linkedin: {
description: 'AWS EC2 Instance Creation Using Ansible Playbook Automation',media: 'https://arkit.co.in/wp-content/uploads/2019/01/AWS-EC2-Instance-Creation-Using-Ansible-Playbook.jpg'                }},
click: function(api, options){
api.simulateClick();
api.openPopup('linkedin');
}});
var $_shareContainer=$(".sharrre-container"),
$_header=$('#header'),
$_postEntry=$('.entry'),
$window=$(window),
startSharePosition=$_shareContainer.offset(),
contentBottom=$_postEntry.offset().top + $_postEntry.outerHeight(),
topOfTemplate=$_header.offset().top,
topSpacing=_setTopSpacing();
shareScroll=function(){
var scrollTop=$window.scrollTop() + topOfTemplate,
stopLocation=contentBottom - ($_shareContainer.outerHeight() + topSpacing);
$_shareContainer.css({position:'fixed'});
if(scrollTop > stopLocation){
$_shareContainer.css({ position:'relative' });
$_shareContainer.offset({
top: contentBottom - $_shareContainer.outerHeight(),
left: startSharePosition.left,
}
);
}
else if(scrollTop >=$_postEntry.offset().top - topSpacing){
$_shareContainer.css({ position:'fixed',top: '100px' });
$_shareContainer.offset({
left: startSharePosition.left,
}
);
}else if(scrollTop < startSharePosition.top +(topSpacing - 1)){
$_shareContainer.css({ position:'relative' });
$_shareContainer.offset({
top: $_postEntry.offset().top,
left:startSharePosition.left,
}
);
}},
shareMove=function(){
startSharePosition=$_shareContainer.offset();
contentBottom=$_postEntry.offset().top + $_postEntry.outerHeight();
topOfTemplate=$_header.offset().top;
_setTopSpacing();
};
setTimeout(function(){
contentBottom=$_postEntry.offset().top + $_postEntry.outerHeight();
}, 2000);
function _setTopSpacing(){
var distanceFromTop=20;
if($window.width() > 1024){
topSpacing=distanceFromTop + $('.nav-wrap').outerHeight();
}else{
topSpacing=distanceFromTop;
}
return topSpacing;
}
$window.scroll(_.throttle(function(){
if($window.width() > 719){
shareScroll();
}else{
$_shareContainer.css({
top:'',
left:'',
position:''
})
}}, 50));
$window.resize(_.debounce(function(){
if($window.width() > 719){
shareMove();
}else{
$_shareContainer.css({
top:'',
left:'',
position:''
})
}}, 50));
});</script>
<script>jQuery(function($){
czrapp.proRelPostsRendered=$.Deferred();
var waypoint=new Waypoint({
element: document.getElementById('pro-related-posts-wrapper'),
handler: function(direction){
if('pending'==czrapp.proRelPostsRendered.state()){
var $wrap=$('#pro-related-posts-wrapper');
$wrap.addClass('loading');
czrapp.doAjax({
action: "ha_inject_pro_related",
related_post_id:7164,
pro_related_posts_opt:{"id":"pro_related_posts_czr_module","title":"","enable":true,"col_number":"2","display_heading":true,"heading_text":"You may also like...","freescroll":true,"ajax_enabled":true,"post_number":10,"order_by":"rand","related_by":"all"},
free_related_posts_opt:"categories",
layout_class:"col-2cl"
}).done(function(r){
if(r&&r.data&&r.data.html){
if('pending'==czrapp.proRelPostsRendered.state()){
$.when($('#pro-related-posts-wrapper').append(r.data.html)).done(function(){
czrapp.proRelPostsRendered.resolve();
$wrap.find('.czr-css-loader').css('opacity', 0);
_.delay(function(){
$wrap.removeClass('loading').addClass('loaded');
}, 800);
});
}}
});
}},
offset: '110%'
});
});</script>
<script defer="defer" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/platform.js" gapi_processed="true"></script>
<script defer="defer" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/6f1cn_002.js" type="text/javascript"></script>
<!--[if lt IE 9]><script defer src="//arkit.co.in/wp-content/cache/wpfc-minified/2bk5bq3c/6f1co.js"></script><![endif]-->
<script>document.addEventListener('DOMContentLoaded',function(){function wpfcgl(){var wgh=document.querySelector('noscript#wpfc-google-fonts').innerText, wgha=wgh.match(/<link[^\>]+>/gi);for(i=0;i<wgha.length;i++){var wrpr=document.createElement('div');wrpr.innerHTML=wgha[i];document.body.appendChild(wrpr.firstChild);}}wpfcgl();});</script>

<link rel="stylesheet" id="tc-front-gfonts" href="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/css.css"><link id="hu-user-gfont" href="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/css_002.css" rel="stylesheet" type="text/css"><iframe name="oauth2relay812899996" id="oauth2relay812899996" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/postmessageRelay.htm" style="width: 1px; height: 1px; position: absolute; top: -100px;" tabindex="-1" aria-hidden="true"></iframe><div style="display: block; visibility: hidden; position: absolute; width: 106px; left: -10000px; top: -10000px;"><table dir="ltr" style="width:106px;" frame="void" rules="none" class=" gc-bubbleDefault pls-container" cellspacing="0" cellpadding="0"><tbody><tr class="gc-reset"><td class="pls-topLeft gc-reset"><img class="gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/border_3.gif"></td><td class="pls-topTail gc-reset"><img class="pls-tailbottom gc-reset" style="width:15px !important; height:9px !important; max-width: 15px !important; max-height: 9px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"><img class="pls-spacerbottom gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"></td><td class="pls-topRight gc-reset"><img class="gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/border_3.gif"></td></tr><tr class="gc-reset"><td class="pls-vertShimLeft gc-reset"><img class="gc-reset" style="width:1px !important; height:4px !important; max-width: 1px !important; max-height: 4px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"></td><td class="pls-vertShim gc-reset"><img class="gc-reset" style="width:1px !important; height:4px !important; max-width: 1px !important; max-height: 4px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"></td><td class="pls-vertShimRight gc-reset"><img class="pls-dropTR gc-reset" style="width:5px !important; height:4px !important; max-width: 5px !important; max-height: 4px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"></td></tr><tr class="gc-reset"><td class="pls-contentLeft gc-reset"><img class="pls-tailright gc-reset" style="width:9px !important; height:15px !important; max-width: 9px !important; max-height: 15px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"><img class="pls-spacerright gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"></td><td class="pls-contentWrap gc-reset"><div class="goog-bubble-content gc-reset"><iframe ng-non-bindable="" hspace="0" marginheight="0" marginwidth="0" scrolling="no" style="margin:0px;position:absolute;z-index:1;border-style:none;outline:none;width:100px;" tabindex="0" vspace="0" id="I0_1556471900569" name="I0_1556471900569" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/subscribe_embed_002.htm" width="100%" frameborder="0"></iframe></div></td><td class="pls-dropRight gc-reset"><img class="pls-tailleft gc-reset" style="width:12px !important; height:19px !important; max-width: 12px !important; max-height: 19px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"><img class="pls-spacerleft gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"></td></tr><tr class="gc-reset"><td class="pls-bottomLeft gc-reset"><img class="gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/border_3.gif"></td><td class="gc-reset"><table style="width:100%" class="gc-reset" cellspacing="0" cellpadding="0"><tbody><tr class="gc-reset"><td class="pls-vert gc-reset"><img class="pls-dropBL gc-reset" style="width:4px !important; height:5px !important; max-width: 4px !important; max-height: 5px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"></td><td class="pls-dropBottom gc-reset"><img class="pls-tailtop gc-reset" style="width:19px !important; height:13px !important; max-width: 19px !important; max-height: 13px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"><img class="pls-spacertop gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"></td></tr></tbody></table></td><td class="pls-vert gc-reset"><img class="pls-dropBR gc-reset" style="width:5px !important; height:5px !important; max-width: 5px !important; max-height: 5px !important;" src="AWS%20EC2%20Instance%20Creation%20Using%20Ansible%20Playbook%20Automation_files/spacer.gif"></td></tr></tbody></table></div></body></html>
<!-- WP Fastest Cache file was created in 0.75467705726624 seconds, on 28-04-19 0:11:13 -->