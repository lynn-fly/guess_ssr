安装说明
使用python工具，管理环境启动，以免每次单独启动

安装ptyhon
pip install supervisor
安装步骤
1.mkdir …/etc/supervisor.d/
2.vim …/etc/supervisord.conf
参考配置

;[unix_http_server]
;file=/data/data/com.termux/files/usr/var/run/supervisor.sock ; the path to the socket file
;chmod=0700 ; socket file mode (default 0700)
;chown=nobody:nogroup ; socket file uid:gid owner
;username=user ; default is no username (open server)
;password=123 ; default is no password (open server)

[inet_http_server] ; inet (TCP) server disabled by default
port=127.0.0.1:9001 ; ip_address:port specifier, *:port for all iface
;username=user ; default is no username (open server)
;password=123 ; default is no password (open server)

[supervisord]
logfile=/usr/local/var/log/supervisord.log ; main log file; default $CWD/supervisord.log
logfile_maxbytes=50MB ; max main logfile bytes b4 rotation; default 50MB
logfile_backups=10 ; # of main logfile backups; 0 means none, default 10
loglevel=info ; log level; default info; others: debug,warn,trace
pidfile=/usr/local/var/run/supervisord.pid ; supervisord pidfile; default supervisord.pid
nodaemon=false ; start in foreground if true; default false
minfds=1024 ; min. avail startup file descriptors; default 1024
minprocs=200 ; min. avail process descriptors;default 200
;umask=022 ; process file creation umask; default 022
;user=supervisord ; setuid to this UNIX account at startup; recommended if root
;identifier=supervisor ; supervisord identifier, default is ‘supervisor’
;directory=/tmp ; default is not to cd during start
;nocleanup=true ; don’t clean up tempfiles at start; default false
;childlogdir=/tmp ; ‘AUTO’ child log dir, default $TEMP
;environment=KEY=“value” ; key value pairs to add to environment
;strip_ansi=false ; strip ansi escape codes in logs; def. false

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
;serverurl=unix:///data/data/com.termux/files/usr/var/run/supervisor.sock ; use a unix:// URL for a unix socket
serverurl=http://127.0.0.1:9001 ; use an http:// url to specify an inet socket
;username=chris ; should be same as in [_http_server] if set
;password=123 ; should be same as in [_http_server] if set
;prompt=mysupervisor ; cmd line prompt (default “supervisor”)
;history_file=~/.sc_history ; use readline history if available

[include]
files = /usr/local/etc/supervisor.d/*.ini

5.添加服务进程
touch …/etc/supervisor.d/nginx.ini
nginx配置参考 （其余配置均可参考）
[program:nginx]
process_name=%(program_name)s_%(process_num)02d
command=/data/data/com.termux/files/usr/bin/nginx -c /usr/etc/nginx/nginx.conf
autostart=true
autorestart=true
user=u0_a414
numprocs=1

touch …/etc/supervisor.d/php-fpm.ini
touch …/etc/supervisor.d/mariadb.ini

启动 supervisord
查看命令 supervisorctl