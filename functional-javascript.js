function makeAnotherFunction(param) {
        let numberOfCalls = 0;
        function self() {
            return numberOfCalls++;
        }
        function otherFunction() {}
        self.publicFunction = () => console.log('it worked!');
        return self;
}
eyesGaming = makeAnotherFunction()
eyesGaming.publicFunction()
console.log(eyesGaming())
console.log(eyesGaming())
console.log(eyesGaming())
console.log(eyesGaming())
