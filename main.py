# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FollowersHub Packages API",
    description="Backend API for serving Instagram growth packages",
    version="1.0.0"
)

# CORS – allow your frontend domain (localhost + production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# --------------------------------------------------------------
# 📦 PACKAGES – bilkul wahi data jo frontend me tha (copy-paste)
# --------------------------------------------------------------
PACKAGES = [
    {
        "id": 1,
        "title": "5K Followers",
        "type": "followers",
        "price": 198,
        "desc": "Real • Active • Permanent",
        "popular": False,
        "discount": False,
    },
    {
        "id": 2,
        "title": "10K Followers",
        "type": "followers",
        "price": 298,
        "desc": "Real • Active • Permanent",
        "popular": True,
        "discount": True,
    },
    {
        "id": 3,
        "title": "20K Followers",
        "type": "followers",
        "price": 549,
        "desc": "Real • Active • Permanent",
        "popular": False,
        "discount": True,
    },
    {
        "id": 4,
        "title": "50K Followers",
        "type": "followers",
        "price": 999,
        "desc": "Real • Active • Permanent",
        "popular": False,
        "discount": False,
    },
    {
        "id": 5,
        "title": "100K Followers",
        "type": "followers",
        "price": 1749,
        "desc": "Real • Active • Permanent",
        "popular": True,
        "discount": True,
    },
    {
        "id": 6,
        "title": "Story Views 5K",
        "type": "views",
        "price": 110,
        "desc": "Ultra-fast • Refill",
        "popular": False,
        "discount": False,
    },
    {
        "id": 7,
        "title": "Story Views 10k",
        "type": "views",
        "price": 179,
        "desc": "Ultra-fast • Refill",
        "popular": False,
        "discount": True,
    },
    {
        "id": 8,
        "title": "Story Views 15k",
        "type": "views",
        "price": 239,
        "desc": "Ultra-fast • Refill",
        "popular": False,
        "discount": False,
    },
    {
        "id": 9,
        "title": "Story Views 20K",
        "type": "views",
        "price": 299,
        "desc": "Ultra-fast • Refill",
        "popular": True,
        "discount": True,
    },
    {
        "id": 10,
        "title": "Blue Tick",
        "type": "verify",
        "price": 299,
        "desc": "Lifetime Verified Badge",
        "popular": False,
        "discount": False,
    },
    {
        "id": 11,
        "title": "Reels Boost 10K",
        "type": "views",
        "price": 199,
        "desc": "High-retention • Instant",
        "popular": False,
        "discount": False,
    },
    {
        "id": 12,
        "title": "Reels Boost 25K",
        "type": "views",
        "price": 399,
        "desc": "Explore • High Reach",
        "popular": True,
        "discount": True,
    },
]

# --------------------------------------------------------------
# 🔌 API ENDPOINTS
# --------------------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "FollowersHub Packages API",
        "endpoints": {
            "all_packages": "/packages",
            "filter_by_type": "/packages/{type}  (followers, views, verify)"
        }
    }

@app.get("/packages")
def get_all_packages():
    """Saare packages ek saath bhejta hai"""
    return {"packages": PACKAGES}

@app.get("/packages/{type}")
def get_packages_by_type(type: str):
    """Sirf ek specific type ke packages (e.g. followers / views / verify)"""
    filtered = [pkg for pkg in PACKAGES if pkg["type"] == type]
    return {"packages": filtered}