
from dragonfly import Repeat, Pause, Function, Choice, MappingRule

from castervoice.lib.actions import Key, Mouse, Text

from castervoice.lib.merge.additions import IntegerRefST
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R

from castervoice.lib import github_automation
from castervoice.lib.temporary import Store, Retrieve

class ChromeExtraRule(MappingRule):
    mapping = {
        "jump <jumpchoice>":
            R(Key("f6/10,c-a/10,del/10") + Text(
                "%(jumpchoice)s") + Key("enter")),
        
        "[show] (extensions|plugins)":
            R(Key("a-f/20, l, e/15, enter")),
        "more tools":
            R(Key("a-f/5, l")),
        
        
        "Outlook mail":
            R(Key("cs-1/5")),
            "Outlook calendar":
            R(Key("cs-2/5")),
            "Outlook people":
            R(Key("cs-3/5")),
            "Outlook to do":
            R(Key("cs-4/5")),
            "Outlook inbox":
            R(Key("g/5,i/5")),
            "Outlook sent":
            R(Key("g/5,s/5")),
            "Outlook draft":
            R(Key("g/5,d/5")),
            "delete mail":
            R(Key("del/5")),
            "outlook read":
            R(Key("q/5")),
            "outlook unread":
            R(Key("u/5")),
            "outlook reply":
            R(Key("r/5")),
            "outlook reply all":
            R(Key("s-r/5")),
"Teams activity":
            R(Key("cs-1/5")),
            "Teams chat":
            R(Key("cs-2/5")),
            "teams":
            R(Key("cs-3/5")),
            "Teams to do":
            R(Key("cs-4/5")),
            "Teams next":
            R(Key("a-down/5")),
            "Teams previous":
            R(Key("a-up/5")),
            "Teams compose":
            R(Key("as-c/5,cs-x")),
            "reply to thread":
            R(Key("as-r/5")),
            "teams send":
            R(Key("c-enter/5")),
            "Teams unread":
            R(Key("u/5")),
            "Teams reply":
            R(Key("r/5")),
            "Teams reply all":
            R(Key("s-r/5")),

    }
    extras = [
        Choice("nth", {
                "first": "1",
                "second": "2",
                "third": "3",
                "fourth": "4",
                "fifth": "5",
                "sixth": "6",
                "seventh": "7",
                "eighth": "8",
            }),
        Choice("jumpchoice", {
                "task board": "https://msazure.visualstudio.com/One/_sprints/taskboard/IoT-Solutions-TwilightSparkle/One/IoT/2110",
                "pull request": "https://msazure.visualstudio.com/One/_git/azure-iots-saas/pullrequests?_a=mine",
                "Outlook": "https://outlook.office365.com/mail/inbox",
                "SharePoint": "https://microsoft.sharepoint.com",
                "teams": "https://teams.microsoft.com",
                "icm": "https://portal.microsofticm.com/imp/v3/incidents/search/advanced",
                "hr": "https://microsoft.sharepoint.com/sites/hrw/Pages/home.aspx",
                "pipelines": "https://msazure.visualstudio.com/One/_build",
            "Facebook": "https://www.facebook.com",
            }),

        IntegerRefST("n", 1, 100),
        IntegerRefST("m", 1, 10)
    ]
    defaults = {"n": 1, "m":"", "nth": ""}


def get_rule():
    return ChromeExtraRule, RuleDetails(name="Chrome extension", executable="chrome")
