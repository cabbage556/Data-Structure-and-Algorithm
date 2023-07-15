class City {
    constructor(name) {
        this.name = name;
        this.routes = new Map();
    }

    addRoute(city, price) {
        this.routes.set(city, price);
    }
}

module.exports = City;
