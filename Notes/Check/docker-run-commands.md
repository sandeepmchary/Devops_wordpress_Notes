<div class="flex flex-col min-h-screen main-wrap">

<header class="w-full px-6 bg-white border-b border-gray-400 fixed linuxize-shadow z-50" id="header">

<nav class="w-full mx-auto flex items-center h-12 justify-start md:h-16">[<span class="font-medium hidden md:block text-md tracking-tight">Linuxize</span>](/)

<div class="flex -mb-px flex-1 min-w-0 text-sm">[<span class="inline-block font-bold md:py-4 md:py-6 py-3">Ubuntu</span> ](/tags/ubuntu/)[<span class="inline-block font-bold md:py-4 md:py-6 py-3">Centos</span> ](/tags/centos/)[<span class="inline-block font-bold md:py-4 md:py-6 py-3">Debian</span> ](/tags/debian/)[<span class="inline-block font-bold md:py-4 md:py-6 py-3">Commands</span> ](/tags/terminal/)[<span class="inline-block font-bold md:py-4 md:py-6 py-3">Series</span> ](/series/)[<span class="inline-block font-bold md:py-4 md:py-6 py-3">Donate</span>](https://www.buymeacoffee.com/8swZOSU6I)</div>

</nav>

</header>

<main class="w-full flex-grow flex-shrink-0 pb-8 pt-16 sm:pt-24 main">

<article class="relative single-post"><span id="ezoic-pub-ad-placeholder-101" class="ezoic-adpicker-ad"></span>

<div class="w-full mx-auto px-6 post-width">

<div class="mb-4 post-header xl:mb-8">

# How to List Containers in Docker

<div class="flex flex-col font-medium md:flex-row text-gray-700 text-xs">

<div class="inline-flex flex-row">

<span>Posted </span><time class="" datetime="2019-11-20T21:31:47+01:00">Nov 20, 2019</time>

<span class="inline-block mx-2">•</span>

4 min read

</div>

</div>

</div>

<div class="lg:flex">

<div class="w-full lg:max-h-full lg:overflow-visible lg:static min-h-screen">

<div class="flex">

<div class="w-full pb-8"><span id="ezoic-pub-ad-placeholder-141" class="ezoic-adpicker-ad"></span>

<div class="flex flex-col xl:flex-relative xl:flex-row">

<aside class="w-full block hidden sidebar2 xxl:block" id="sidebar2">

<div class="w-full -mt-12 flex-col hidden justify-between pb-4 pt-12 sticky top-16 xl:flex">

<div class="bg-gray-200 mb-6 p-4 pb-2 overflow-auto table-of-contents toc">

Contents

<div class="relative overflow-hidden">

<div class="lg:max-h-toc overflow-y-auto scrollbar-thumb-gray scrollbar-thumb-rounded scrollbar-track-gray-lighter scrollbar-w-2 scrolling-touch">

<nav id="TableOfContents">

*   [List Docker Containers](#list-docker-containers)
*   [Conclusion](#conclusion)

</nav>

</div>

</div>

Share

<section class="w-full mx-auto">

<nav class="flex flex-wrap">[](https://twitter.com/share?text=How%20to%20List%20Containers%20in%20Docker&url=https%3a%2f%2flinuxize.com%2fpost%2fhow-to-list-docker-containers%2f)[](https://www.facebook.com/sharer/sharer.php?caption=How%20to%20List%20Containers%20in%20Docker&u=https%3a%2f%2flinuxize.com%2fpost%2fhow-to-list-docker-containers%2f)[](https://pinterest.com/pin/create/button/?url=https%3a%2f%2flinuxize.com%2fpost%2fhow-to-list-docker-containers%2f&media=https%3a%2f%2flinuxize.com%2fpost%2fhow-to-list-docker-containers%2ffeatured.jpg&description=How%20to%20List%20Containers%20in%20Docker)[](https://plus.google.com/share?url=https%3a%2f%2flinuxize.com%2fpost%2fhow-to-list-docker-containers%2f)[](https://news.ycombinator.com/submitlink?t=How%20to%20List%20Containers%20in%20Docker&u=https%3a%2f%2flinuxize.com%2fpost%2fhow-to-list-docker-containers%2f)[](mailto:?subject=How%20to%20List%20Containers%20in%20Docker&body=Check%20out%20this%20article:%0A%0Ahttps%3a%2f%2flinuxize.com%2fpost%2fhow-to-list-docker-containers%2f)</nav>

</section>

</div>

<span id="ezoic-pub-ad-placeholder-152" class="ezoic-adpicker-ad"></span></div>

</aside>

<section class="w-full mx-auto lg:ml-0 lg:mr-auto lg:pr-6 min-w-0 xl:mx-0 xl:w-full xxl:px-6">

<figure class="relative -mx-6 lg:mx-0 mb-6">

<div class="w-full mx-auto my-0 block relative">

<div class="w-full h-full absolute inset-0 m-auto bg-gray-200 overflow-hidden">![](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8+PXHfwAJnAPfCuZXlQAAAABJRU5ErkJggg==)

<noscript>![](/post/how-to-list-docker-containers/featured.jpg)</noscript>

</div>

</div>

</figure>

<div class="markdown">

Docker is a containerization platform that allows you to quickly build, test, and deploy applications as portable, self-sufficient containers that can run virtually anywhere. It is the de-facto standard for container deployment, and it is an essential tool for DevOps engineers and their continuous integration and delivery pipeline.

In this article, we'll explain how to list Docker containers.<span id="ezoic-pub-ad-placeholder-158" class="ezoic-adpicker-ad"></span>

## List Docker Containers

The Docker command for listing containers takes the following form:<span id="ezoic-pub-ad-placeholder-138" class="ezoic-adpicker-ad"></span>

    docker container ls [options]

Older Docker versions before 1.13 are using a different command to list the containers:

    docker ps [options]

The command above is still supported in newer Docker versions where the `ps` command is an alias to `container ls`.<span id="ezoic-pub-ad-placeholder-139" class="ezoic-adpicker-ad"></span><span style="display:block !important;float:none;margin-bottom:24px !important;margin-left:0px !important;margin-right:0px !important;margin-top:24px !important;min-height:90px;min-width:728px;text-align:center !important;" class="ezoic-ad box-3 adtester-container adtester-container-139" data-ez-name="linuxize_com-box-3"><span id="div-gpt-ad-linuxize_com-box-3-0" ezaw="728" ezah="90" style="position:relative;z-index:0;display:inline-block;min-height:90px;min-width:728px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[728,90],'linuxize_com-box-3','ezslot_9',139,'0','0']));</script></span></span>

To list the running container run the `docker container ls` command without any option:<span id="ezoic-pub-ad-placeholder-156" class="ezoic-adpicker-ad"></span>

    docker container ls

<span id="ezoic-pub-ad-placeholder-159" class="ezoic-adpicker-ad"></span>The output will look something like this:<span id="ezoic-pub-ad-placeholder-140" class="ezoic-adpicker-ad"></span><span style="display:block !important;float:none;margin-bottom:24px !important;margin-left:0px !important;margin-right:0px !important;margin-top:24px !important;min-height:280px;min-width:336px;text-align:center !important;" class="ezoic-ad medrectangle-3 adtester-container adtester-container-140" data-ez-name="linuxize_com-medrectangle-3"><span id="div-gpt-ad-linuxize_com-medrectangle-3-0" ezaw="336" ezah="280" style="position:relative;z-index:0;display:inline-block;min-height:280px;min-width:336px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[336,280],'linuxize_com-medrectangle-3','ezslot_8',140,'0','0']));</script></span></span>

    CONTAINER ID    IMAGE        COMMAND                  CREATED        STATUS        PORTS       NAMES
    c8bded53da86    postgres     "docker-entrypoint.s…"   2 hours ago    Up 2 hours    5432/tcp    pg
    571c3a115fcf    redis        "docker-entrypoint.s…"   4 hours ago    Up 4 hours    6379/tcp    cache
    05ef6d8680ba    nginx        "nginx -g 'daemon of…"   2 hours ago    Up 2 hours    80/tcp      web

Each line of the output includes the following columns:

*   `Container ID` – A unique alphanumeric string that identifies each container.
*   `Image` – The Docker image used to create the container.
*   `Command` – The command that is executed when starting the container.
*   `Created` – The creation time of the container.
*   `Status` – The status of the container.
*   `Ports` – The container's published ports.
*   `Name` – The name of the container.

If there are no running containers, only the header line is displayed.

The `-a`, `--all` option tells `docker container ls` to print a list of all containers:

    docker container ls -a

    CONTAINER ID    IMAGE        COMMAND                  CREATED        STATUS                    PORTS       NAMES
    b28cbaa91f15    couchbase    "/entrypoint.sh couc…"   5 hours ago    Exited (0) 3 hours ago                db
    c8bded53da86    postgres     "docker-entrypoint.s…"   2 hours ago    Up 2 hours                5432/tcp    pg
    571c3a115fcf    redis        "docker-entrypoint.s…"   4 hours ago    Up 4 hours                6379/tcp    cache
    05ef6d8680ba    nginx        "nginx -g 'daemon of…"   2 hours ago    Up 2 hours                80/tcp      web

By default, columns with a length exceeding a specified limit are truncated. Use the `--no-trunc` option to disable truncation:

    docker container ls --no-trunc

To only display the containers’ IDs pass the `-q`, `--quiet` option:<span id="ezoic-pub-ad-placeholder-142" class="ezoic-adpicker-ad"></span><span style="display:block !important;float:none;margin-bottom:24px !important;margin-left:0px !important;margin-right:0px !important;margin-top:24px !important;min-height:280px;min-width:336px;text-align:center !important;" class="ezoic-ad medrectangle-4 adtester-container adtester-container-142" data-ez-name="linuxize_com-medrectangle-4"><span id="div-gpt-ad-linuxize_com-medrectangle-4-0" ezaw="336" ezah="280" style="position:relative;z-index:0;display:inline-block;min-height:280px;min-width:336px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[336,280],'linuxize_com-medrectangle-4','ezslot_10',142,'0','0']));</script></span></span>

    docker container ls -q

    c8bded53da86
    571c3a115fcf
    05ef6d8680ba

The `--format` allows you to format the output using a Go template. For example to print only the containers’ names and status including the header you would run:<span id="ezoic-pub-ad-placeholder-160" class="ezoic-adpicker-ad"></span>

    docker container ls --format 'table {{.Names}}\t{{.Status}}'

    NAMES    STATUS
    pg       Up 2 hours
    cache    Up 4 hours
    web      Up 2 hours

Use the `-s`, `--size` option to view the size of the containers:

    docker container ls -s

Each line will include a column named `SIZE` that shows the container size:

    CONTAINER ID    IMAGE        COMMAND                  CREATED        STATUS        PORTS       NAMES    SIZE
    c8bded53da86    postgres     "docker-entrypoint.s…"   2 hours ago    Up 2 hours    5432/tcp    pg       63B (virtual 394MB)
    571c3a115fcf    redis        "docker-entrypoint.s…"   4 hours ago    Up 4 hours    6379/tcp    cache    0B (virtual 98.2MB)
    05ef6d8680ba    nginx        "nginx -g 'daemon of…"   2 hours ago    Up 2 hours    80/tcp      web      2B (virtual 126MB)

The `--last`, `-n` option tells the command to display `n` last created containers, including all states. For example, to view the latest two created containers you would run:<span id="ezoic-pub-ad-placeholder-143" class="ezoic-adpicker-ad"></span><span style="display:block !important;float:none;margin-bottom:6px !important;margin-left:0px !important;margin-right:0px !important;margin-top:6px !important;min-height:250px;min-width:300px;text-align:center !important;" class="ezoic-ad box-4 adtester-container adtester-container-143" data-ez-name="linuxize_com-box-4"><span id="div-gpt-ad-linuxize_com-box-4-0" ezaw="300" ezah="250" style="position:relative;z-index:0;display:inline-block;min-height:250px;min-width:300px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[300,250],'linuxize_com-box-4','ezslot_11',143,'0','0']));</script></span></span>

    docker container ls -n 2

    CONTAINER ID    IMAGE        COMMAND                  CREATED        STATUS                    PORTS       NAMES
    b28cbaa91f15    couchbase    "/entrypoint.sh couc…"   5 hours ago    Exited (0) 3 hours ago                db
    c8bded53da86    postgres     "docker-entrypoint.s…"   2 hours ago    Up 2 hours                5432/tcp    pg

<span id="ezoic-pub-ad-placeholder-161" class="ezoic-adpicker-ad"></span>There is also an option to list only the latest created container `--latest` , `-l` which is same as `-n 1`:

    docker container ls -l

The `--filter`, `-f` option allows you to filter the output based on certain criteria. For example, to view only the containers with status `exited` you would run:

    docker container ls -f "status=exited"

    CONTAINER ID    IMAGE        COMMAND                  CREATED        STATUS                    PORTS       NAMES
    b28cbaa91f15    couchbase    "/entrypoint.sh couc…"   5 hours ago    Exited (0) 3 hours ago                db

For a list of all supported filters check the [Docker documentation](https://docs.docker.com/engine/reference/commandline/ps/#filtering)<span id="ezoic-pub-ad-placeholder-144" class="ezoic-adpicker-ad"></span><span style="display:block !important;float:none;margin-bottom:0 !important;margin-left:0px !important;margin-right:0px !important;margin-top:24px !important;min-width:160px;text-align:center !important;" class="ezoic-ad link-v-med-1 adtester-container adtester-container-144" data-ez-name="linuxize_com-link-v-med-1"></span>

## Conclusion

A Docker container is a standalone runtime instance of an image.

To list Docker containers, use the `docker container ls` command or its alias `docker ps`.<span id="ezoic-pub-ad-placeholder-157" class="ezoic-adpicker-ad"></span><span style="display:block !important;float:none;margin-bottom:2px !important;margin-left:0px !important;margin-right:0px !important;margin-top:10px !important;min-height:400px;min-width:580px;text-align:center !important;" class="ezoic-ad large-mobile-banner-1 adtester-container adtester-container-157" data-ez-name="linuxize_com-large-mobile-banner-1"><span id="div-gpt-ad-linuxize_com-large-mobile-banner-1-0" ezaw="580" ezah="400" style="position:relative;z-index:0;display:inline-block;min-height:400px;min-width:580px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[580,400],'linuxize_com-large-mobile-banner-1','ezslot_12',157,'0','0']));</script></span></span>

If you have any questions, please leave a comment below.<span id="ezoic-pub-ad-placeholder-145" class="ezoic-adpicker-ad"></span>

<div class="flex flex-wrap my-6">[docker](/tags/docker/)</div>

</div>

</section>

</div>

<span id="ezoic-pub-ad-placeholder-102" class="ezoic-adpicker-ad"></span></div>

</div>

</div>

<div class="w-full absolute hidden -mb-16 flex-grow lg:-mb-0 lg:block lg:pt-0 lg:static sidebar top-16 z-40" id="sidebar"><span id="ezoic-pub-ad-placeholder-126" class="ezoic-adpicker-ad"></span><span style="display:block !important;float:none;margin-left:auto !important;margin-right:auto !important;min-height:1050px;min-width:300px;text-align:center !important;width:300px;" class="ezoic-ad box-1 adtester-container adtester-container-126" data-ez-name="linuxize_com-box-1"><span style="display:block !important;float:none;margin-bottom:6px !important;margin-left:0px !important;margin-right:0px !important;margin-top:0 !important;min-height:250px;min-width:300px;text-align:center !important;" class="ezoic-ad box-1 adtester-container adtester-container-126" data-ez-name="linuxize_com-box-1"><span id="div-gpt-ad-linuxize_com-box-1-0" ezaw="300" ezah="262" style="position:relative;z-index:0;display:inline-block;min-height:262px;min-width:300px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[300,250],'linuxize_com-box-1','ezslot_4',126,'0','0']));</script></span></span><span style="display:block !important;float:none;margin-bottom:6px !important;margin-left:0px !important;margin-right:0px !important;margin-top:0 !important;min-height:250px;min-width:300px;text-align:center !important;" class="ezoic-ad box-1 adtester-container adtester-container-126" data-ez-name="linuxize_com-box-1"><span id="div-gpt-ad-linuxize_com-box-1-0_1" ezaw="300" ezah="262" style="position:relative;z-index:0;display:inline-block;min-height:262px;min-width:300px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[300,250],'linuxize_com-box-1','ezslot_5',126,'0','1']));</script></span></span><span style="display:block !important;float:none;margin-bottom:6px !important;margin-left:0px !important;margin-right:0px !important;margin-top:0 !important;min-height:250px;min-width:300px;text-align:center !important;" class="ezoic-ad box-1 adtester-container adtester-container-126" data-ez-name="linuxize_com-box-1"><span id="div-gpt-ad-linuxize_com-box-1-0_2" ezaw="300" ezah="262" style="position:relative;z-index:0;display:inline-block;min-height:262px;min-width:300px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[300,250],'linuxize_com-box-1','ezslot_6',126,'0','2']));</script></span></span><span style="display:block !important;float:none;margin-bottom:6px !important;margin-left:0px !important;margin-right:0px !important;margin-top:0 !important;min-height:250px;min-width:300px;text-align:center !important;" class="ezoic-ad box-1 adtester-container adtester-container-126" data-ez-name="linuxize_com-box-1"><span id="div-gpt-ad-linuxize_com-box-1-0_3" ezaw="300" ezah="262" style="position:relative;z-index:0;display:inline-block;min-height:262px;min-width:300px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[300,250],'linuxize_com-box-1','ezslot_7',126,'0','3']));</script></span></span></span>

<div class="bg-gray-200 mb-6 p-4 pb-2 related-content">

Related Tutorials

*   [Docker Run Command with Examples](https://linuxize.com/post/docker-run-command/)
*   [How to Connect to a Docker Container](https://linuxize.com/post/how-to-connect-to-docker-container/)
*   [How To Install and Use Docker on Debian 10 Linux](https://linuxize.com/post/how-to-install-and-use-docker-on-debian-10/)
*   [How To Install and Use Docker on Raspberry Pi](https://linuxize.com/post/how-to-install-and-use-docker-on-raspberry-pi/)
*   [How to Build Docker Images with Dockerfile](https://linuxize.com/post/how-to-build-docker-images-with-dockerfile/)
*   [How To Install and Use Docker Compose on Debian 9](https://linuxize.com/post/how-to-install-and-use-docker-compose-on-debian-9/)
*   [How To Remove Docker Containers, Images, Volumes, and Networks](https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/)

</div>

<div class="flex flex-col -mt-12 lg:block lg:relative lg:sticky lg:top-16 pt-12">

<div class="sideblock">

<div class="hidden affiliate">[](https://www.vultr.com/?ref=6812257)</div>

</div>

</div>

<span id="ezoic-pub-ad-placeholder-105" class="ezoic-adpicker-ad"></span><span style="display:block !important;float:none;margin-left:auto !important;margin-right:auto !important;min-height:1050px;min-width:300px;text-align:center !important;width:300px;" class="ezoic-ad large-leaderboard-1 adtester-container adtester-container-105" data-ez-name="linuxize_com-large-leaderboard-1"><span style="display:block !important;float:none;margin-bottom:6px !important;margin-left:0px !important;margin-right:0px !important;margin-top:0 !important;min-height:250px;min-width:300px;text-align:center !important;" class="ezoic-ad large-leaderboard-1 adtester-container adtester-container-105" data-ez-name="linuxize_com-large-leaderboard-1"><span id="div-gpt-ad-linuxize_com-large-leaderboard-1-0" ezaw="300" ezah="262" style="position:relative;z-index:0;display:inline-block;min-height:262px;min-width:300px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[300,250],'linuxize_com-large-leaderboard-1','ezslot_0',105,'0','0']));</script></span></span><span style="display:block !important;float:none;margin-bottom:6px !important;margin-left:0px !important;margin-right:0px !important;margin-top:0 !important;min-height:250px;min-width:300px;text-align:center !important;" class="ezoic-ad large-leaderboard-1 adtester-container adtester-container-105" data-ez-name="linuxize_com-large-leaderboard-1"><span id="div-gpt-ad-linuxize_com-large-leaderboard-1-0_1" ezaw="300" ezah="262" style="position:relative;z-index:0;display:inline-block;min-height:262px;min-width:300px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[300,250],'linuxize_com-large-leaderboard-1','ezslot_1',105,'0','1']));</script></span></span><span style="display:block !important;float:none;margin-bottom:6px !important;margin-left:0px !important;margin-right:0px !important;margin-top:0 !important;min-height:250px;min-width:300px;text-align:center !important;" class="ezoic-ad large-leaderboard-1 adtester-container adtester-container-105" data-ez-name="linuxize_com-large-leaderboard-1"><span id="div-gpt-ad-linuxize_com-large-leaderboard-1-0_2" ezaw="300" ezah="262" style="position:relative;z-index:0;display:inline-block;min-height:262px;min-width:300px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[300,250],'linuxize_com-large-leaderboard-1','ezslot_2',105,'0','2']));</script></span></span><span style="display:block !important;float:none;margin-bottom:6px !important;margin-left:0px !important;margin-right:0px !important;margin-top:0 !important;min-height:250px;min-width:300px;text-align:center !important;" class="ezoic-ad large-leaderboard-1 adtester-container adtester-container-105" data-ez-name="linuxize_com-large-leaderboard-1"><span id="div-gpt-ad-linuxize_com-large-leaderboard-1-0_3" ezaw="300" ezah="262" style="position:relative;z-index:0;display:inline-block;min-height:262px;min-width:300px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[300,250],'linuxize_com-large-leaderboard-1','ezslot_3',105,'0','3']));</script></span></span></span></div>

</div>

</div>

</article>

<div class="px-6">

<section class="w-full mx-auto border-gray-200 border-t mt-8 pt-8 max-w-article">

<div class="p-8 sm:py-8 bg-orange-100">

If you like our content, please consider buying us a coffee.  
Thank you for your support!

<div class="w-full mx-auto flex items-center flex-col max-w-sm sm:flex-row justify-center mt-6">[<span class="font-medium ml-2 text-xs uppercase">Buy me a coffee</span>](https://www.buymeacoffee.com/8swZOSU6I)</div>

</div>

</section>

<section class="w-full mx-auto border-gray-200 border-t mt-8 pt-8 max-w-article">

<div class="bg-gray-200 p-8 sm:py-8">

Sign up to our newsletter and get our latest tutorials and news straight to your mailbox.

<form action="https://linuxize.us17.list-manage.com/subscribe/post?u=35cd4cd9d021c25c3dd7cabfd&amp;id=9cfa4c89de" class="pt-8" id="mc-embedded-subscribe-form" method="post" name="mc-embedded-subscribe-form" novalidate="">

<div class="w-full mx-auto flex items-center flex-col max-w-sm sm:flex-row justify-between mb-2"><input class="w-full block bg-white appearance-none border hover:border-gray-700 mb-3 px-4 py-3 rounded sm:mb-0 text-gray-800" name="EMAIL" aria-label="email" placeholder="Your email..." type="email"> <input class="hidden" name="b_35cd4cd9d021c25c3dd7cabfd_9cfa4c89de" tabindex="-1"> <button class="w-full px-4 py-3 rounded bg-indigo-700 hover:bg-indigo-800 sm:ml-4 sm:w-auto text-white tracking-wide" name="subscribe" type="submit"><span class="text-center">Subscribe</span></button></div>

We’ll never share your email address or spam you.

</form>

</div>

</section>

<section class="w-full mx-auto border-gray-200 border-t mt-8 pt-8 max-w-5xl">

<div class="flex flex-wrap -mx-4">[

<div class="w-full flex flex-col h-full">

Nov 26, 2019

<div class="text-gray-800 mb-2 flex-grow font-normal md:mb-4 text-lg">Docker Run Command with Examples</div>

<div>

<figure class="relative">

<div class="w-full mx-auto my-0 block relative">

<div class="w-full h-full absolute inset-0 m-auto bg-gray-200 overflow-hidden">![](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8+PXHfwAJnAPfCuZXlQAAAABJRU5ErkJggg==)

<noscript>![](/post/docker-run-command/featured.jpg)</noscript>

</div>

</div>

</figure>

</div>

</div>

](https://linuxize.com/post/docker-run-command/)[

<div class="w-full flex flex-col h-full">

Oct 4, 2019

<div class="text-gray-800 mb-2 flex-grow font-normal md:mb-4 text-lg">How to Connect to a Docker Container</div>

<div>

<figure class="relative">

<div class="w-full mx-auto my-0 block relative">

<div class="w-full h-full absolute inset-0 m-auto bg-gray-200 overflow-hidden">![](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8+PXHfwAJnAPfCuZXlQAAAABJRU5ErkJggg==)

<noscript>![](/post/how-to-connect-to-docker-container/featured.jpg)</noscript>

</div>

</div>

</figure>

</div>

</div>

](https://linuxize.com/post/how-to-connect-to-docker-container/)[

<div class="w-full flex flex-col h-full">

Jul 30, 2019

<div class="text-gray-800 mb-2 flex-grow font-normal md:mb-4 text-lg">How To Install and Use Docker on Debian 10 Linux</div>

<div>

<figure class="relative">

<div class="w-full mx-auto my-0 block relative">

<div class="w-full h-full absolute inset-0 m-auto bg-gray-200 overflow-hidden">![](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8+PXHfwAJnAPfCuZXlQAAAABJRU5ErkJggg==)

<noscript>![](/post/how-to-install-and-use-docker-on-debian-10/featured.jpg)</noscript>

</div>

</div>

</figure>

</div>

</div>

](https://linuxize.com/post/how-to-install-and-use-docker-on-debian-10/)</div>

</section>

<section class="w-full mx-auto relative border-gray-200 border-t max-w-3xl mt-8 pt-16 py-8">[Write a comment](https://linuxize.com/post/how-to-list-docker-containers/#disqus_thread "Show comments for post")

<noscript>Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)</noscript>

</section>

</div>

</main>

<section class="w-full absolute inset-0 bg-white block h-screen hidden search z-100" id="search-box">

<div class="flex flex-col min-h-screen">

<header class="w-full mx-auto flex items-center h-12 justify-end px-6 sm:h-16 z-10">[<small class="block text-center sm:w-8 w-6">ESC</small>](#)</header>

<div class="w-full px-6 flex-grow flex-shrink-0 pb-8 pt-16 sm:pt-24">

<div class="flex flex-col mx-auto max-w-screen-xl mb-4 mb-8">

<footer class="mt-6">[](https://www.algolia.com/doc/)</footer>

</div>

</div>

</div>

</section>

<footer class="w-full px-6 bg-gray-100">

<div class="w-full mx-auto flex items-center justify-center flex-wrap lg:justify-between lg:text-left max-w-screen-xl py-8 text-center">

<div class="w-full lg:w-1/2 lg:mb-0 mb-2 text-sm">

<div class="w-full block lg:flex lg:items-center lg:w-auto">

<div class="lg:flex-grow"><span class="block text-gray-800 lg:inline-block lg:mb-0 lg:mr-8 mb-2">© 2019 Linuxize.com</span> [Privacy Policy](/privacy-policy/) [Contact](/contact/)</div>

</div>

</div>

<div class="w-full flex justify-center lg:justify-end lg:w-1/2">[](https://twitter.com/linuxize)[](https://www.facebook.com/linuxize/)[](/index.xml)</div>

</div>

<span id="ezoic-pub-ad-placeholder-128" class="ezoic-adpicker-ad"></span></footer>

</div>

<script type="text/javascript">(function(f,a){function g(b,a,c){b.addEventListener?b.addEventListener(a,c):b.attachEvent("on"+a,function(){c.call(b)})}function k(b){b&&("string"==typeof b["class"]&&b["class"]&&a.getElementById("uglipop_popbox").setAttribute("class",b["class"]),b.keepLayout&&!b["class"]&&a.getElementById("uglipop_popbox").setAttribute("style","position:relative;height:300px;width:300px;background-color:white;opacity:1;"),"string"==typeof b.content&&b.content&&"html"==b.source&&(a.getElementById("uglipop_popbox").innerHTML=b.content),"string"==typeof b.content&&b.content&&"div"==b.source&&(a.getElementById("uglipop_popbox").innerHTML=a.getElementById(b.content).innerHTML));a.getElementById("uglipop_overlay_wrapper").style.display="";a.getElementById("uglipop_overlay").style.display="";a.getElementById("uglipop_content_fixed").style.display=""}function h(){a.getElementById("uglipop_overlay_wrapper").style.display="none";a.getElementById("uglipop_overlay").style.display="none";a.getElementById("uglipop_content_fixed").style.display="none"}g(a,"DOMContentLoaded",function(){var b=a.createElement("div"),e=a.createElement("div"),c=a.createElement("div"),d=a.createElement("div");e.id="uglipop_content_fixed";e.setAttribute("style","position:fixed;top: 50%;left: 50%;transform: translate(-50%, -50%);-webkit-transform: translate(-50%, -50%);-ms-transform: translate(-50%, -50%);opacity:1;z-index:10000000;");c.id="uglipop_popbox";d.id="uglipop_overlay_wrapper";d.setAttribute("style","position:absolute;top:0;bottom:0;left:0;right:0;display:none");b.id="uglipop_overlay";b.setAttribute("style","position:fixed;top:0;bottom:0;left:0;right:0;opacity:0.3;width:100%;height:100%;background-color:black;");d.appendChild(b);e.appendChild(c);a.body.appendChild(d);a.body.appendChild(e);a.getElementById("uglipop_overlay_wrapper").style.display="none";a.getElementById("uglipop_overlay").style.display="none";a.getElementById("uglipop_content_fixed").style.display="none";d.addEventListener("click",h);g(f,"keydown",function(a){27==a.keyCode&&h()});f.uglipop=k})})(window,document); var ezRBA = (function() { function init() { var reportAdsBtns = document.querySelectorAll('.ez-report-ad-button'); for (var i = 0; i < reportAdsBtns.length; i++) { reportAdsBtns[i].addEventListener('click', function(e) { var url = '<iframe src="https://ezoic.com/pub/reportads/reportads.html' + e.target.getAttribute('name') + '" width="400" height="500" style="border-radius: 10px; box-shadow: 2px 2px 30px 6px rgba(0,0,0,0.75); border: 1px solid black;"></iframe>' uglipop({ class: 'none', source: 'html', content: url, }); }); } function bindEvent(element, eventName, eventHandler) { if (element.addEventListener) { element.addEventListener(eventName, eventHandler, false); } else if (element.attachEvent) { element.attachEvent('on' + eventName, eventHandler); } } bindEvent(window, 'message', function(e) { if (e.data === 'close-report-ad-modal') { document.getElementById('uglipop_overlay_wrapper').style.display = 'none'; document.getElementById('uglipop_overlay').style.display = 'none'; document.getElementById('uglipop_content_fixed').style.display = 'none'; } }) } return { init: init }; })(); ezRBA.init();</script> <script type="text/javascript">(function(){function e(b,a){for(var d=0;d<a.length;d++){var f=a[d];if(0==f.complete||"undefined"!=typeof f.readyState&&4>f.readyState){var h=f.getAttribute("src")||f.currentSrc;"undefined"!=typeof f.readyState&&0==f.readyState?f.addEventListener("loadstart",function(g){var k=g.getAttribute("src")||g.currentSrc;l(g,k)}):(h=f.getAttribute("src")||f.currentSrc,l(f,h));f.addEventListener("load",function(g){var k=g.currentTarget.getAttribute("src")||g.srcElement.currentSrc;m(g,k)});f.addEventListener("loadeddata", function(g){var k=g.currentTarget.getAttribute("src")||g.srcElement.currentSrc;m(g,k)});f.addEventListener("error",function(g){var k=g.currentTarget.getAttribute("src")||g.srcElement.currentSrc;m(g,k)})}}}function c(b){for(var a=0;a<document.styleSheets.length;a++)if(document.styleSheets[a].href==b)return!0;return!1}e("img",document.querySelectorAll("img"));e("video",document.querySelectorAll("video"));e("audio",document.querySelectorAll("audio"));(function(b){for(var a=0;a<b.length;a++){var d=b[a]; if(("preload"==d.getAttribute("rel")||"stylesheet"==d.getAttribute("rel"))&&null!=d.getAttribute("href")&&c(d.getAttribute("href"))){l(d,d.getAttribute("href"));var f=document.createElement("img");f.onerror=function(h){m(d,h.path[0].currentSrc)};f.src=d.getAttribute("href")}}})(document.querySelectorAll("link"))})();</script> <script type="text/javascript" style="display:none;">var __ez_dims = (function() { var setCookie = function( name, content, expiry ) { return document.cookie = name+'='+content+((expiry)?';expires='+(new Date(Math.floor(new Date().getTime()+expiry*1000)).toUTCString()):'')+';path=/'; }; var ffid = 1; var oh = window.screen.height; var ow = window.screen.width; var h = ffid === 1 ? oh : (oh > ow) ? oh : ow; var w = ffid === 1 ? ow : (oh > ow) ? ow : oh; var uh = window.innerHeight || document.documentElement.clientHeight || document.getElementsByTagName('body')[0].clientHeight; var uw = window.innerWidth || document.documentElement.clientWidth || document.getElementsByTagName('body')[0].clientWidth; setCookie('ezds', encodeURIComponent('ffid='+ffid+',w='+w+',h='+h), (31536e3*7)); setCookie('ezohw', encodeURIComponent('w='+uw+',h='+uh), (31536e3*7)); })();</script> <script type="text/javascript" style="display:none;" async="">__ez.queue.addFile('edmonton.php', '/detroitchicago/edmonton.webp?a=a&cb=188-0&shcb=32', true, [], true, false, false, false); __ez.queue.addFile('jellyfish.php', '/porpoiseant/jellyfish.webp?a=a&cb=188-0&shcb=32', false, [], true, false, false, false);</script> <script>var _audins_dom="linuxize_com",_audins_did=93605;__ez.queue.addDelayFunc("audins.js","__ez.script.add", "//go.ezoic.net/detroitchicago/audins.js?cb=188-0");</script>

<noscript>

<div style="display:none;">![Quantcast](//pixel.quantserve.com/pixel/p-31iz6hfFutd16.gif?labels=Domain.linuxize_com,DomainId.93605)</div>

</noscript>

<noscript>![](https://sb.scorecardresearch.com/p?c1=2&c2=20015427&cv=2.0&cj=1)</noscript>