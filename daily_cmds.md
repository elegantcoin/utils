# my commonly used Linux_command_lines

<p align="center">
    <a href="https://github.com/elegantcoin/utils"><img src="https://img.shields.io/badge/status-updating-brightgreen.svg"></a>
    <a href="https://github.com/python/cpython"><img src="https://img.shields.io/badge/Python-3.7-FF1493.svg"></a>
    <a href="https://github.com/elegantcoin/utils"><img src="https://img.shields.io/badge/platform-Windows%7CLinux%7CmacOS-660066.svg"></a>
    <a href="https://opensource.org/licenses/mit-license.php"><img src="https://badges.frapsoft.com/os/mit/mit.svg"></a>
    <a href="https://github.com/elegantcoin/utils/stargazers"><img src="https://img.shields.io/github/stars/elegantcoin/utils.svg?logo=github"></a>
    <a href="https://github.com/elegantcoin/utils/network/members"><img src="https://img.shields.io/github/forks/elegantcoin/utils.svg?color=blue&logo=github"></a>
    <a href="https://www.python.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" align="right" height="48" width="48" ></a>
</p>
<br />

## :fire:Terminal终端:
-   `git remote set-url origin https://codeXXXXXXXXXXXXXXXXXXXX@github.com/elegantcoin/utils.git` 登录git
-   `rsync --bwlimit=1000 -artP file1 -e 'ssh -p xxxx' user@targetmachine:file2`
-   `cat cmd_lines_2022-05_15.log|egrep -E "history lines |\(103\)"`
-   `split -l 1000 -a 3 bigfiles.txt smallfiles.txt` split files
-   `mysql/redis-cli -h service -P xxxx -u username -p password` mysql
-   `docker ps` docker
-   `docker exec -it 100 /bin/bash`
-   `keys * / get key 100` redis
-   `tar -cvf compress.tar /filefolder --exclude=./.ssh` tar
-   `tar cf /tmp/compress.tar /big/tree --exclude-from <(find /big/tree -size +3M)` tar
-   `tar czf /tmp/compress.tar |split -b 1000m - small-file.tar` split tar file
-   `find /tmp/path -3M|xargs tar cf /tmp/compress.tar` tar fills <3M in path
-   `find ./ -name "*" -size +3M` find files >3M
-   `find ./ -name "*.txt|xargs cat >3.txt"` cat into one file
-   `wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh` get ananconda
-   `vim ~/.bash_history`
-   `vim ~/.bashrc`
-   `vim ~/.bash_profile`
-   `nohup jupyter 2>&1 &` nohup
-   `jupyter notebook >jupyter.log 2>&1 &`
-   `ps -aux |egrep test.sh|egrep -v grep|awk '${print $0}'|sort -k 2 -n`
-   `ps -aux|egrep python |xargs  kill -9` careful if root user
-   `ps -eo pid,sgi_p,cmd --sort sgi_p|egrep "python"`
-   `magick -loop 0 -delay 10 fram*.jpg frame.gif` generate gifs
-   `rsvg-convert -z 10.0 pprof001_true.svg >pprof001.png` convert to png
-   `tree -df` tree dir
-   `tree -L 3` tree 3 levels
-   `tree -dfIL "*anaconda*|*git*" 3` tree ignore keywords
-   `rename 's/\.jpeg/\.jpg' *.jpeg` rename using regx
-   `cat my_log.log|egrep ''$'\t123'$'\tsname'|sort -k 1 -k 2` egrep \t and sort
-   `ls --sort=none` no sorting when ls(useful in huge files folder)
-   `aek '! a[$0]++'` drop duplicate
-   `sed -i'.bak' 's/words/word/g'  my_log.log` replace global
-   `head my_log.log|awk -F ',' '{printf("%s %s\n",split($0,var_arr,","),var_arr[1])}' `print lines?
-   `python -m cProfile my_script.py` cProfile
-   `go tool pprof cpu.out` go Profile
-   `/bin/spark2-submit --master yarn --deploy-mode client --queue username --driver-memory 32g --executor-cores 10 --executor-memory 32g` spark
-   

```bash
    # Python zip() behavior in bash
    file_names=$(ls *.txt)
    file_arr=($file_names)
    var_arr=($file_arr)
    i=0
    for s_one in $file_names;do
    ((i++))
    my_count=$(cat $s_one |wc -l)
    my_content=$(sed 's/\\n/\\\\n/g' $s_one)
    echo "${var_arr[${i}]}"
    echo "#\n#${s_one}|${my_count}\n\n${my_content}\n\n" >>all.txt
    mv file_$i.qgz file${s_one}.qgz
```
-   ``
```bash
    # function in bash
    auto_triger() {
        msg=$1
        echo ${msg}
    }
    auto_triger "this is a func"
```
-   ``
```bash
    # crontab -l -e
    30 09 * * * cd /tmp/robot && sh start_robot.sh >>robot.log 2>&1
```
-   ``
-   ``
-   ``
-   ``
-   ``
-   ``
-   ``
-   ``
-   ``
-   ``
-   ``
-   ``
-   ``




。。。。。。（待续）

  
  
  - 另外参见[Linux各目录的详细介绍](https://www.cnblogs.com/dengyungao/p/8426878.html)
  - 另外参见[命令行的艺术]https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md



