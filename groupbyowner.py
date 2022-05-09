def group(files_in):
    t = ''
    l = []
    #files = {k:v for k, v in sorted(files_in.items(), key=by_value)}
    new_file = {}
    def by_value(item):
        return item[1]
    
    new_files_sor = {k:v for k, v in sorted(files.items(), key=by_value)}
    #new_files = {value: []+[key] for key,value in files.items()}
    #t = ''
    #l = []
    #files = {k:v for k, v in sorted(files_in.items(), key=by_value)}
    #new_file = {}
    
    for key,value in new_files_sor.items():
        #print(t, value)
        if t == value:
            new_file[value].append(key)
        else:
            new_file[value]=[key]
            #print(new_file)
        t = value
                
    return(new_file)

if __name__ == "__main__":
    files = {
        'input.txt': 'Randy',
        'code.py': 'Sandy',
        'output.txt': 'Randy'
    }
    print(group(files))