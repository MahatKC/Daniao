class ProductPipeline:
    pipeline = []

    def add_cypher(self, function, function_param):
        self.pipeline.append([function, function_param])
        
    def __str__(self) -> str:
       x=repr(dict(zip(range(len(self.pipeline)),[[function.__name__, function_param] for function, function_param in self.pipeline])))
       return x

    def remove_cypher(self, index):
        self.pipeline.pop(index)

    def run(self, plaintext):
        temporary_cyphertext = plaintext
        for function, function_param in self.pipeline:
            temporary_cyphertext = function(temporary_cyphertext, function_param)

        return temporary_cyphertext

