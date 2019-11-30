// Test for Postman 

var body = pm.response.json();

var schema = {
    "acres": { "type": "float" },
    "coordinates": { "type": ["object", "null"] },
    "crop": { "type": ["string", "null"] },
    "efficiency": { "type": "float" },
    "id": { "type": "float" }
};

var coordinates_schema = {
    "coordinates": { "type": ["array", "null"] }
}

// Status code is 200
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test('Schema is valid', function () {
    pm.expect(tv4.validate(body, schema)).to.be.true;
});

pm.test('Coordinates schema is valid', function () {
    pm.expect(tv4.validate(body.coordinates, coordinates_schema)).to.be.true;
});

pm.test("Check if field object contains all provided keys", function () {
    pm.expect(body).to.have.all.keys(
        'acres',
        'coordinates',
        'crop',
        'efficiency',
        'id'
    );
});

pm.test("Check if coordinates contains all provided keys", function () {
    pm.expect(body.coordinates).to.have.all.keys(
        'coordinates'
    );
});

pm.test("Efficiency score is 0 or 1", function () {
    pm.expect(body.efficiency).to.be.oneOf([0, 1]);
});

pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});


