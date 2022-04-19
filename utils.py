from pickle import load

def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text

def load_set(filename):
    doc = load_doc(filename)
    dataset = list()
    
    # process line by line
    for line in doc.split('\n'):
        # skip empty lines
        if(len(line) < 1):
            continue
        
        # get image name
        name = line.split('.')[0]
        dataset.append(name)
    return list(set(dataset))

def load_photo_features(filename, dataset):
    # load all features
    all_features = load(open(filename), 'rb')
    # filter features
    features = {k: all_features[k] for k in dataset}
    return features