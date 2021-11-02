from dragonfly import Mimic, Function, MappingRule, Choice, Pause, Dictation

from castervoice.lib.actions import Key, Text

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.additions import IntegerRefST
from castervoice.lib.merge.state.short import R


def _apply(n):
    if n != 0:
        Text("stash@{" + str(int(n)) + "}").execute()


class GitBashExtensionRule(MappingRule):
    GIT_ADD_ALL = "g, i, t, space, a, d, d, space, minus, A"
    GIT_COMMIT = "g, i, t, space, c, o, m, m, i, t, space, minus, m, space, quote, quote, left"
    HISTORY_SEARCH = "h, i, s, t, o, r, y, space, | , space, g, r, e, p, space, space, quote, quote, left"
    mapping = {
       
        "(git|get) log mine":
            R(Text("git log -n 15 --oneline --author=\"George\"")),
        "(git|get) log":
            R(Text("git log -n 15 ")),
  
        "display branch":
            R(Text("git branch  | grep '*' | sed 's/* //'")+ Key("enter")),
        "search shell":
            R(Key("apps:down,f")),
        "search history":
            R(Key(HISTORY_SEARCH)),  
        "execute history <n>":
            R(Text("!%(n)d ")),        
        "shell break":
            R( Key("c-c") ),
         "push d <dirs>":
            R(Text("pushd %(dirs)s")),
        "bring me <dirs>":
            R(Text("cd %(dirs)s") + Key("enter")),
        "bring me up":
            R(Text("cd ..") + Key("enter")),
        "list":
            R(Text("ls")),
        "make directory":
            R(Text("mkdir ")),
        "merge develop | (git|get) merge develop":
            R(Text("git fetch origin && git merge origin/develop")+Key("enter/580,c-x/80")),

        "undo [last] commit | (git|get) reset soft head":
            R(Text("git reset --soft HEAD~1")),
        "(undo changes | (git|get) reset hard)":
            R(Text("git reset --hard")),
         
        "grape filter <text>":
            R(Text("| grep \"%(text)s\" ")),
        "to file":
            R(Text(" > FILENAME")),
        "docker":
            R(Text("docker")),
        "docker build":
            R(Text("sudo docker build . ")),
        "docker add arg":
            R(Text("--build-arg")+Key("space,quote,colon,quote")),
       
       
        "show file":
            R(Text("cat -n ")),
        "show file line <n>":
            R(Text("sed -n %(n)dp")),


        "dot net build":
            R(Text("sudo dotnet build")),
        "dot net test":
            R(Text("sudo dotnet test")),  
        "python three activate":
            R(Text("source ~/python-enviroments/p3/bin/activate")),
        
        #CONEMU
        "tab <m>":
            R(Key("c-%(m)s")),
        "switch tab":
            R(Key("w-q")),

       #azure voice assist pack#

         "azure login":
            R(Text("sudo az login")),
        "copy line <n>":
            R(Key("s-left/20,up:%(n)d,home/30,s-end/100,c-insert")),
        "select line up <n>":
            R(Key("s-left/20,up:%(n)d,home/30,s-end/100")),
        "select line down <n>":
            R(Key("s-left/20,down:%(n)d,home/30,s-end/100")),
        "copy device code":
            R(Key("s-left/20,up,home/30,right:100/50,s-right:8/50, c-insert/30,w-1/20")+Pause("20")+Key("c-t,c-l")+Text("aka.ms/devicelogin")),

         "azure group list":
        R(Text("sudo az group list | jq '.[] | .id'")),

        "azure account list":
        R(Text("sudo az account list | jq '.[] | .name'")),
         "azure account show":
        R(Text("sudo az account show")+Key("enter")),

        ## setting active azure subscription from clipboard
         "azure account set":
        R(Text("sudo az account set -s")+ Key("s-insert")),
        
        "iot environment":
        R(Text("echo iotcsub=$iotcsub env=$iotcenv iotcappid=$iotcappid iotcdeviceid=$iotcdeviceid iotcgroup=$iotcgroup")+Key("enter")),

        
        "iot use production":
        R(Text("export iotcenv=azureiotcentral.com")+Key("enter/10")+Text("echo $iotcenv")+Key("enter/10")),

        ## set active subscription to be used in creating iot central app  from clipboard
        "iot subscription set":
        R(Text("export iotcsub=")+Key("s-insert/10,enter/10")+Text("echo $iotcsub")+Key("enter/10")),

        ## set active resource group to be used in creating iot central app  from clipboard
        "iot group set":
        R(Text("export iotcgroup=")+Key("s-insert/10,enter/10")+Text("echo $iotcgroup")+Key("enter/10")),
        
        ## list IOT Central applications
         "iot application list":
        R(Text("sudo az iot central app list | jq '.[] | {\"appid\":.applicationId,\"name\":.name, \"subdomain\":.subdomain}'")+Key("enter")),
        
        ## create IOT Central application 
        "iot application create":
        R(Text("sudo az iot central app create -g $iotcgroup -s $iotcsub -n ")),

        # Set active IOT Central application id
        "iot application set":
        R(Text("export iotcappid=")+Key("s-insert/10,enter/10")+Text("echo $iotcappid")+Key("enter/10"),
             rdescript="az iotc:set application ID variable"),
        # set active IOT Central device name
        "iot device set":
        R(Text("export iotcdeviceid=")+Key("s-insert/10,enter/10")+Text("echo $iotcdeviceid")+Key("enter/10"),
             rdescript="az iotc:set device ID variable"),
        # Create IOT Central device
        "iot device create":
        R(Mimic("iot", "environment")+Key("enter")+Text("sudo az iot central device create --app-id $iotcappid --subscription $iotcsub --central-dns-suffix $iotcenv --device-id $iotcdeviceid")),
        # Display IOT Central device creds
        "iot device credentials":
        R(Text("sudo az iot central device show-credentials --app-id $iotcappid --subscription $iotcsub --central-dns-suffix $iotcenv --device-id $iotcdeviceid")),
    
    }
    extras = [
        IntegerRefST("n", 1, 100000000),
        IntegerRefST("m", 1, 10),
        Dictation("text"),
        Choice("dockerid",{
                    "hub": "dockerid",
                    }),
        Choice("dirs",
                    {
                    "scripts": "~/scripts",
                    "shell home":"~/",
                    }),
    ]
    defaults = {"n": 0, "text": ""}


_executables = [
    "\\sh.exe",
    "\\bash.exe",
    "\\cmd.exe",
    "\\mintty.exe",
    "\\powershell.exe",
    "\\ConEmu64.exe",
    "idea",
    "idea64",
    "studio64",
    "pycharm"
]


def get_rule():
    return GitBashExtensionRule, RuleDetails(name="git bash extensions", executable=_executables)

