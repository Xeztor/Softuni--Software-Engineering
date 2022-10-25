class footballTeam {
    constructor(clubName, country) {
        this.clubName = clubName;
        this.country = country;
        this.invitedPlayers = [];
        this.playerNames = [];
    };

    newAdditions(footballPlayers) {
        let invited = [];
        for (let playerString of footballPlayers) {
            let [name, age, value] = playerString.split('/');
            age = Number(age);
            value = Number(value);
            if (this.playerNames.includes(name)) {
                let playerIndex = this.playerNames.indexOf(name);
                let playerValue = this.invitedPlayers[playerIndex].value;
                if (playerValue < value) {
                    this.invitedPlayers[playerIndex].value = value;
                };
                continue

            };

            invited.push(name);
            this.playerNames.push(name);

            let playerObj = {
                name,
                age,
                value,
            };
            this.invitedPlayers.push(playerObj)

        };

        return "You successfully invite " + invited.join(', ') + '.'
        // return "You successfully invite " + `${invited.join(', ')}`
    };

    signContract(selcetedPlayer) {
        let [name, offer] = selcetedPlayer.split('/');
        if (!this.playerNames.includes(name)) {
            throw new Error(`${name} is not invited to the selection list!`);
        };

        let playerIndex = this.playerNames.indexOf(name);
        let player = this.invitedPlayers[playerIndex];

        if (offer < player.value) {
            throw new Error(`The manager's offer is not enough to sign a contract with ${name}, ${player.value - offer} million more are needed to sign the contract!`)
        };

        player.value = 'Bought'

        return `Congratulations! You sign a contract with ${name} for ${offer} million dollars.`
    };

    ageLimit(name, age) {
        if (!this.playerNames.includes(name)) {
            throw new Error(`${name} is not invited to the selection list!`)
        };

        let player = this._getPlayerByindex(name);

        if (player.age < age) {
            if (age - player.age < 5) {
                return `${name} will sign a contract for ${age - player.age} years with ${this.clubName} in ${this.country}!`
            }
            return `${name} will sign a full 5 years contract for ${this.clubName} in ${this.country}!`
        }

        return `${name} is above age limit!`
    };

    transferWindowResult() {
        let output = "Players list:\n"
        let playersStrings =
            this.invitedPlayers
                .sort((a, b) => a.name.localeCompare(b.name))
                .map(player => `Player ${player.name}-${player.value}`)
        return output + playersStrings.join('\n')
    };

    _getPlayerByindex(name) {
        let playerIndex = this.playerNames.indexOf(name);
        let player = this.invitedPlayers[playerIndex];
        return player;
    }

}

let team = new footballTeam('pesho', 'bg');

console.log(team.newAdditions(["Kylian Mbappé/23/160", "Lionel Messi/35/50", "Pau Torres/25/52", "Lionel Messi/35/60"]));

console.log(team.signContract("Kylian Mbappé/160"));
try {
    console.log(team.signContract("gosho/60"));
} catch (err) {
    console.log('Error: ' + err.message);
};

try {
    console.log(team.ageLimit('pesho'))
} catch (err) {
    console.log('Error: ' + err.message)
}
console.log(team.ageLimit('Kylian Mbappé', 25))
console.log(team.ageLimit('Pau Torres', 30))
console.log(team.ageLimit('Lionel Messi', 34))

console.log(team.transferWindowResult())
