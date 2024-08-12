# app/helpers/decorators.py

def transform_id(func):
    """Decorator to transform _id to id in the returned list of documents."""
    def wrapper(*args, **kwargs):
        # Call the original function
        results = func(*args, **kwargs)
        
        # Transform _id to id in each document
        for document in results:
            if '_id' in document:
                document['id'] = document.pop('_id')
        return results
    
    return wrapper
