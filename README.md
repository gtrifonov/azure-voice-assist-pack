# azure-voice-assist-pack
This repository contains  extensions to Caster application rules to use Dragon dictation in azure devops workflows.

To learn more about how intsall and configure Caster with Nuance Dragon Natural Speaking visit https://caster.readthedocs.io/en/latest/

## Examples:

### MS Teams:
- Say 'call to <person>' to call specific predefined contact
- Say 'join next' to join next scheduled meeting
- Say 'teams bring me to <teams>' to navigate to defined team

### Bash:
- Say 'azure login' to execute az login
- Say 'azure copy device code' to copy device code when prompted and navigate to aka.ms/devicelogin

Each playbook contains sequence of voice commands to complete azure cli scenario 

## Azure IOT Central voice playbook 
- open gitbash terminal
- say <code>"azure login"</code>
- say "copy device code": System will open aka.ms/devicelogin and you can use voice commands to finish login flow
- switch back to terminal
- say "azure account list"
- say "grape filter <mysubscription>" where <mysubscription> is a filter phrase to minimize amount of accounts to be returned
- use voice commands to copy to clipboard required subscription name
- say "iot subscription set"
- say "azure group list" + "grape filter <group>" where is a filter phrase to minimize amount of resource groups to be returned
- use voice commands to copy to clipboard required group name
- say "iot group set"
- you can verify which iot enviroments values you have by saying "iot environment"
- say "iot application create" and dictate application name
- use voice commands to copy appid from previous command output
- say "iot application set"
- use voice commands to copy to clipboard desired device name
- say "iot device create"

## Resources:
- Caster git - https://github.com/dictation-toolbox/Caster
- DragonFly git - https://github.com/dictation-toolbox/dragonfly
- Dragon Commands Cheet Sheet - https://www.nuance.com/content/dam/nuance/en_us/collateral/dragon/command-cheat-sheet/ct-dragon-naturally-speaking-en-us.pdf
