class HBMessage {
    constructor() {
        this.type = "HB";
        this.timestamp = new Date().toISOString();
    }
}

class TextMessage {
    constructor(msg = "") {
        this.type = "TEXT";
        this.msg = msg;
    }
}

module.exports = { HBMessage, TextMessage };