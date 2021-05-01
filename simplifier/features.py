from . import apsynp
from . import models

def cosine_sim(original, c):
    """Get cosine similarity using vector model."""
    try:
        return models.embeddings.similarity(original, c)
    except KeyError:
        return 0

def apsyn_sim(original, c):
    """Get ApsynP result."""
    try:
        return apsynp.detection(original, c, models.embeddings)[1]
    except KeyError:
        return 0
