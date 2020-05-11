#! /usr/bin/env bash
#
set -u
set +e
# set -o noglob
#
workdir=$(cd "$(dirname $0)" && pwd)
topdir=$(cd "${workdir}" && cd .. && pwd)
scriptdir=${workdir}
cd "${workdir}"
#
# lib: color print
bold=$(tput bold)
green=$(tput setf 2)
red=$(tput setf 4)
reset=$(tput sgr0)

function green() {
	  printf "${bold}${green}%s${reset}\n" "$@";
  }
function red() {
	  printf "${bold}${red}%s${reset}\n" "$@";
  }

# green "hello"
# red "hello"

cat << eof
  __  __          _____           _        _ _           
 |  \/  |        |_   _|         | |      | | |          
 | \  / |_   _     | |  _ __  ___| |_ __ _| | | ___ _ __ 
 | |\/| | | | |    | | | '_ \/ __| __/ _' | | |/ _ \ '__|
 | |  | | |_| |   _| |_| | | \__ \ || (_| | | |  __/ |   
 |_|  |_|\__, |  |_____|_| |_|___/\__\__,_|_|_|\___|_|   
          __/ |                                                            
         |___/                                                             
eof

echo
echo


function install_service(){
  cd "${scriptdir}"
  cp myframework.service /usr/lib/systemd/system
  systemctl daemon-reload
  systemctl enable myframework.service
  systemctl restart myframework.service
  systemctl status myframework.service
  echo
}

function uninstall_service(){
  cd "${scriptdir}"
  systemctl stop myframework.service
  systemctl disable myframework.service
  rm -f /usr/lib/systemd/system/myframework.service
  systemctl daemon-reload
  echo
}


function option1(){
  install_service
  green "option1 done!"
}
function option2(){
  uninstall_service
  green "option2 done!"
}
function option3(){
  green "option3 done!"
}
function option4(){
  green "option4 done!"
}
function option5(){
  green "option5 done!"
}
function option6(){
  green "option6 done!"
}
function option7(){
  green "option7 done!"
}
function option8(){
  green "option8 done!"
}
function option9(){
  green "option9 done!"
}
function option10(){
  green "option10 done!"
}
function option11(){
  green "option11 done!"
}
function option12(){
  green "option12 done!"
}


cat << eof
====
1) install service
2) uninstall service
q) quit 
====
eof

while echo; read -p "Enter your option: " option; do
  case $option in
    1)
      option1
      break
      ;;
    2)
      option2
      break
      ;;
    q|Q)
      break
      ;;
    *)
      echo "invalid option, enter again..."
      continue
  esac
done

