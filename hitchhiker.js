let a, b, c, x, y, z;

a = 5;
b = 10;
console.log(`a = ${a}, b = ${b}`);
[a, b] = [b, a];
console.log(">>[a, b = b, a]");
console.log(`Now swapped: a = ${a}, b = ${b}\n`);


a = 9;
b = 11;
c = 44;
[a, [b, c]] = [1, [2, 3]];
console.log("\n >> a, (b, c) = 1, (2, 3)");
console.log(`a = ${a}, b = ${b}, c = ${c}`);
[x, y, z] = [1, 2, 3];
console.log("\n >> x, y, z = 1, 2, 3");
console.log(`x = ${x}, y = ${y}, z = ${z}`);

[a, ...rest] = [1, 2, 3];
console.log("\n >> a, *rest = [1, 2, 3]");
console.log(`a = ${a}, rest = ${rest}`);

[a, b, ...c] = [1, 2, 3, 4, 5, 6];
console.log("\n >> a, b, ...c = [1, 2, 3, 4, 5, 6]");
console.log(`a = ${a}, middle = ${b}, c = ${c}`);

//# sourceMappingURL=hitchhiker.js.map
