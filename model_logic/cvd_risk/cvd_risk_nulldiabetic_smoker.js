function cvd_risk_nulldiabetic_smoker(gender, age, systolic, bmi){
    if(gender == null || age == null || systolic == null || bmi == null) { return null; }
    const data = [
        {"g":"m","ami":40,"ama":44,"smi":0,"sma":120,"bmi":0,"bma":20,"r":2},
        {"g":"m","ami":40,"ama":44,"smi":120,"sma":139,"bmi":0,"bma":20,"r":3},
        {"g":"m","ami":40,"ama":44,"smi":140,"sma":159,"bmi":0,"bma":20,"r":5},
        {"g":"m","ami":40,"ama":44,"smi":160,"sma":179,"bmi":0,"bma":20,"r":7},
        {"g":"m","ami":40,"ama":44,"smi":180,"sma":999,"bmi":0,"bma":20,"r":10},
        {"g":"m","ami":45,"ama":49,"smi":0,"sma":120,"bmi":0,"bma":20,"r":3},
        {"g":"m","ami":45,"ama":49,"smi":120,"sma":139,"bmi":0,"bma":20,"r":4},
        {"g":"m","ami":45,"ama":49,"smi":140,"sma":159,"bmi":0,"bma":20,"r":6},
        {"g":"m","ami":45,"ama":49,"smi":160,"sma":179,"bmi":0,"bma":20,"r":9},
        {"g":"m","ami":45,"ama":49,"smi":180,"sma":999,"bmi":0,"bma":20,"r":13},
        {"g":"m","ami":50,"ama":54,"smi":0,"sma":120,"bmi":0,"bma":20,"r":4},
        {"g":"m","ami":50,"ama":54,"smi":120,"sma":139,"bmi":0,"bma":20,"r":6},
        {"g":"m","ami":50,"ama":54,"smi":140,"sma":159,"bmi":0,"bma":20,"r":8},
        {"g":"m","ami":50,"ama":54,"smi":160,"sma":179,"bmi":0,"bma":20,"r":11},
        {"g":"m","ami":50,"ama":54,"smi":180,"sma":999,"bmi":0,"bma":20,"r":15},
        {"g":"m","ami":55,"ama":59,"smi":0,"sma":120,"bmi":0,"bma":20,"r":6},
        {"g":"m","ami":55,"ama":59,"smi":120,"sma":139,"bmi":0,"bma":20,"r":8},
        {"g":"m","ami":55,"ama":59,"smi":140,"sma":159,"bmi":0,"bma":20,"r":11},
        {"g":"m","ami":55,"ama":59,"smi":160,"sma":179,"bmi":0,"bma":20,"r":14},
        {"g":"m","ami":55,"ama":59,"smi":180,"sma":999,"bmi":0,"bma":20,"r":19},
        {"g":"m","ami":60,"ama":64,"smi":0,"sma":120,"bmi":0,"bma":20,"r":8},
        {"g":"m","ami":60,"ama":64,"smi":120,"sma":139,"bmi":0,"bma":20,"r":10},
        {"g":"m","ami":60,"ama":64,"smi":140,"sma":159,"bmi":0,"bma":20,"r":14},
        {"g":"m","ami":60,"ama":64,"smi":160,"sma":179,"bmi":0,"bma":20,"r":18},
        {"g":"m","ami":60,"ama":64,"smi":180,"sma":999,"bmi":0,"bma":20,"r":23},
        {"g":"m","ami":65,"ama":69,"smi":0,"sma":120,"bmi":0,"bma":20,"r":11},
        {"g":"m","ami":65,"ama":69,"smi":120,"sma":139,"bmi":0,"bma":20,"r":14},
        {"g":"m","ami":65,"ama":69,"smi":140,"sma":159,"bmi":0,"bma":20,"r":18},
        {"g":"m","ami":65,"ama":69,"smi":160,"sma":179,"bmi":0,"bma":20,"r":22},
        {"g":"m","ami":65,"ama":69,"smi":180,"sma":999,"bmi":0,"bma":20,"r":28},
        {"g":"m","ami":70,"ama":74,"smi":0,"sma":120,"bmi":0,"bma":20,"r":15},
        {"g":"m","ami":70,"ama":74,"smi":120,"sma":139,"bmi":0,"bma":20,"r":18},
        {"g":"m","ami":70,"ama":74,"smi":140,"sma":159,"bmi":0,"bma":20,"r":23},
        {"g":"m","ami":70,"ama":74,"smi":160,"sma":179,"bmi":0,"bma":20,"r":28},
        {"g":"m","ami":70,"ama":74,"smi":180,"sma":999,"bmi":0,"bma":20,"r":34},
        {"g":"m","ami":40,"ama":44,"smi":0,"sma":120,"bmi":20,"bma":24,"r":3},
        {"g":"m","ami":40,"ama":44,"smi":120,"sma":139,"bmi":20,"bma":24,"r":4},
        {"g":"m","ami":40,"ama":44,"smi":140,"sma":159,"bmi":20,"bma":24,"r":6},
        {"g":"m","ami":40,"ama":44,"smi":160,"sma":179,"bmi":20,"bma":24,"r":8},
        {"g":"m","ami":40,"ama":44,"smi":180,"sma":999,"bmi":20,"bma":24,"r":12},
        {"g":"m","ami":45,"ama":49,"smi":0,"sma":120,"bmi":20,"bma":24,"r":4},
        {"g":"m","ami":45,"ama":49,"smi":120,"sma":139,"bmi":20,"bma":24,"r":5},
        {"g":"m","ami":45,"ama":49,"smi":140,"sma":159,"bmi":20,"bma":24,"r":7},
        {"g":"m","ami":45,"ama":49,"smi":160,"sma":179,"bmi":20,"bma":24,"r":10},
        {"g":"m","ami":45,"ama":49,"smi":180,"sma":999,"bmi":20,"bma":24,"r":15},
        {"g":"m","ami":50,"ama":54,"smi":0,"sma":120,"bmi":20,"bma":24,"r":5},
        {"g":"m","ami":50,"ama":54,"smi":120,"sma":139,"bmi":20,"bma":24,"r":7},
        {"g":"m","ami":50,"ama":54,"smi":140,"sma":159,"bmi":20,"bma":24,"r":9},
        {"g":"m","ami":50,"ama":54,"smi":160,"sma":179,"bmi":20,"bma":24,"r":13},
        {"g":"m","ami":50,"ama":54,"smi":180,"sma":999,"bmi":20,"bma":24,"r":18},
        {"g":"m","ami":55,"ama":59,"smi":0,"sma":120,"bmi":20,"bma":24,"r":7},
        {"g":"m","ami":55,"ama":59,"smi":120,"sma":139,"bmi":20,"bma":24,"r":9},
        {"g":"m","ami":55,"ama":59,"smi":140,"sma":159,"bmi":20,"bma":24,"r":12},
        {"g":"m","ami":55,"ama":59,"smi":160,"sma":179,"bmi":20,"bma":24,"r":16},
        {"g":"m","ami":55,"ama":59,"smi":180,"sma":999,"bmi":20,"bma":24,"r":21},
        {"g":"m","ami":60,"ama":64,"smi":0,"sma":120,"bmi":20,"bma":24,"r":9},
        {"g":"m","ami":60,"ama":64,"smi":120,"sma":139,"bmi":20,"bma":24,"r":12},
        {"g":"m","ami":60,"ama":64,"smi":140,"sma":159,"bmi":20,"bma":24,"r":15},
        {"g":"m","ami":60,"ama":64,"smi":160,"sma":179,"bmi":20,"bma":24,"r":20},
        {"g":"m","ami":60,"ama":64,"smi":180,"sma":999,"bmi":20,"bma":24,"r":25},
        {"g":"m","ami":65,"ama":69,"smi":0,"sma":120,"bmi":20,"bma":24,"r":12},
        {"g":"m","ami":65,"ama":69,"smi":120,"sma":139,"bmi":20,"bma":24,"r":15},
        {"g":"m","ami":65,"ama":69,"smi":140,"sma":159,"bmi":20,"bma":24,"r":19},
        {"g":"m","ami":65,"ama":69,"smi":160,"sma":179,"bmi":20,"bma":24,"r":24},
        {"g":"m","ami":65,"ama":69,"smi":180,"sma":999,"bmi":20,"bma":24,"r":30},
        {"g":"m","ami":70,"ama":74,"smi":0,"sma":120,"bmi":20,"bma":24,"r":16},
        {"g":"m","ami":70,"ama":74,"smi":120,"sma":139,"bmi":20,"bma":24,"r":20},
        {"g":"m","ami":70,"ama":74,"smi":140,"sma":159,"bmi":20,"bma":24,"r":24},
        {"g":"m","ami":70,"ama":74,"smi":160,"sma":179,"bmi":20,"bma":24,"r":30},
        {"g":"m","ami":70,"ama":74,"smi":180,"sma":999,"bmi":20,"bma":24,"r":36},
        {"g":"m","ami":40,"ama":44,"smi":0,"sma":120,"bmi":25,"bma":29,"r":3},
        {"g":"m","ami":40,"ama":44,"smi":120,"sma":139,"bmi":25,"bma":29,"r":5},
        {"g":"m","ami":40,"ama":44,"smi":140,"sma":159,"bmi":25,"bma":29,"r":7},
        {"g":"m","ami":40,"ama":44,"smi":160,"sma":179,"bmi":25,"bma":29,"r":10},
        {"g":"m","ami":40,"ama":44,"smi":180,"sma":999,"bmi":25,"bma":29,"r":14},
        {"g":"m","ami":45,"ama":49,"smi":0,"sma":120,"bmi":25,"bma":29,"r":4},
        {"g":"m","ami":45,"ama":49,"smi":120,"sma":139,"bmi":25,"bma":29,"r":6},
        {"g":"m","ami":45,"ama":49,"smi":140,"sma":159,"bmi":25,"bma":29,"r":9},
        {"g":"m","ami":45,"ama":49,"smi":160,"sma":179,"bmi":25,"bma":29,"r":12},
        {"g":"m","ami":45,"ama":49,"smi":180,"sma":999,"bmi":25,"bma":29,"r":17},
        {"g":"m","ami":50,"ama":54,"smi":0,"sma":120,"bmi":25,"bma":29,"r":6},
        {"g":"m","ami":50,"ama":54,"smi":120,"sma":139,"bmi":25,"bma":29,"r":8},
        {"g":"m","ami":50,"ama":54,"smi":140,"sma":159,"bmi":25,"bma":29,"r":11},
        {"g":"m","ami":50,"ama":54,"smi":160,"sma":179,"bmi":25,"bma":29,"r":15},
        {"g":"m","ami":50,"ama":54,"smi":180,"sma":999,"bmi":25,"bma":29,"r":20},
        {"g":"m","ami":55,"ama":59,"smi":0,"sma":120,"bmi":25,"bma":29,"r":7},
        {"g":"m","ami":55,"ama":59,"smi":120,"sma":139,"bmi":25,"bma":29,"r":10},
        {"g":"m","ami":55,"ama":59,"smi":140,"sma":159,"bmi":25,"bma":29,"r":13},
        {"g":"m","ami":55,"ama":59,"smi":160,"sma":179,"bmi":25,"bma":29,"r":18},
        {"g":"m","ami":55,"ama":59,"smi":180,"sma":999,"bmi":25,"bma":29,"r":24},
        {"g":"m","ami":60,"ama":64,"smi":0,"sma":120,"bmi":25,"bma":29,"r":10},
        {"g":"m","ami":60,"ama":64,"smi":120,"sma":139,"bmi":25,"bma":29,"r":13},
        {"g":"m","ami":60,"ama":64,"smi":140,"sma":159,"bmi":25,"bma":29,"r":17},
        {"g":"m","ami":60,"ama":64,"smi":160,"sma":179,"bmi":25,"bma":29,"r":22},
        {"g":"m","ami":60,"ama":64,"smi":180,"sma":999,"bmi":25,"bma":29,"r":28},
        {"g":"m","ami":65,"ama":69,"smi":0,"sma":120,"bmi":25,"bma":29,"r":13},
        {"g":"m","ami":65,"ama":69,"smi":120,"sma":139,"bmi":25,"bma":29,"r":16},
        {"g":"m","ami":65,"ama":69,"smi":140,"sma":159,"bmi":25,"bma":29,"r":21},
        {"g":"m","ami":65,"ama":69,"smi":160,"sma":179,"bmi":25,"bma":29,"r":26},
        {"g":"m","ami":65,"ama":69,"smi":180,"sma":999,"bmi":25,"bma":29,"r":33},
        {"g":"m","ami":70,"ama":74,"smi":0,"sma":120,"bmi":25,"bma":29,"r":17},
        {"g":"m","ami":70,"ama":74,"smi":120,"sma":139,"bmi":25,"bma":29,"r":21},
        {"g":"m","ami":70,"ama":74,"smi":140,"sma":159,"bmi":25,"bma":29,"r":26},
        {"g":"m","ami":70,"ama":74,"smi":160,"sma":179,"bmi":25,"bma":29,"r":32},
        {"g":"m","ami":70,"ama":74,"smi":180,"sma":999,"bmi":25,"bma":29,"r":39},
        {"g":"m","ami":40,"ama":44,"smi":0,"sma":120,"bmi":30,"bma":35,"r":4},
        {"g":"m","ami":40,"ama":44,"smi":120,"sma":139,"bmi":30,"bma":35,"r":6},
        {"g":"m","ami":40,"ama":44,"smi":140,"sma":159,"bmi":30,"bma":35,"r":8},
        {"g":"m","ami":40,"ama":44,"smi":160,"sma":179,"bmi":30,"bma":35,"r":12},
        {"g":"m","ami":40,"ama":44,"smi":180,"sma":999,"bmi":30,"bma":35,"r":17},
        {"g":"m","ami":45,"ama":49,"smi":0,"sma":120,"bmi":30,"bma":35,"r":5},
        {"g":"m","ami":45,"ama":49,"smi":120,"sma":139,"bmi":30,"bma":35,"r":7},
        {"g":"m","ami":45,"ama":49,"smi":140,"sma":159,"bmi":30,"bma":35,"r":10},
        {"g":"m","ami":45,"ama":49,"smi":160,"sma":179,"bmi":30,"bma":35,"r":14},
        {"g":"m","ami":45,"ama":49,"smi":180,"sma":999,"bmi":30,"bma":35,"r":20},
        {"g":"m","ami":50,"ama":54,"smi":0,"sma":120,"bmi":30,"bma":35,"r":7},
        {"g":"m","ami":50,"ama":54,"smi":120,"sma":139,"bmi":30,"bma":35,"r":9},
        {"g":"m","ami":50,"ama":54,"smi":140,"sma":159,"bmi":30,"bma":35,"r":12},
        {"g":"m","ami":50,"ama":54,"smi":160,"sma":179,"bmi":30,"bma":35,"r":17},
        {"g":"m","ami":50,"ama":54,"smi":180,"sma":999,"bmi":30,"bma":35,"r":23},
        {"g":"m","ami":55,"ama":59,"smi":0,"sma":120,"bmi":30,"bma":35,"r":8},
        {"g":"m","ami":55,"ama":59,"smi":120,"sma":139,"bmi":30,"bma":35,"r":11},
        {"g":"m","ami":55,"ama":59,"smi":140,"sma":159,"bmi":30,"bma":35,"r":15},
        {"g":"m","ami":55,"ama":59,"smi":160,"sma":179,"bmi":30,"bma":35,"r":20},
        {"g":"m","ami":55,"ama":59,"smi":180,"sma":999,"bmi":30,"bma":35,"r":27},
        {"g":"m","ami":60,"ama":64,"smi":0,"sma":120,"bmi":30,"bma":35,"r":11},
        {"g":"m","ami":60,"ama":64,"smi":120,"sma":139,"bmi":30,"bma":35,"r":14},
        {"g":"m","ami":60,"ama":64,"smi":140,"sma":159,"bmi":30,"bma":35,"r":19},
        {"g":"m","ami":60,"ama":64,"smi":160,"sma":179,"bmi":30,"bma":35,"r":24},
        {"g":"m","ami":60,"ama":64,"smi":180,"sma":999,"bmi":30,"bma":35,"r":31},
        {"g":"m","ami":65,"ama":69,"smi":0,"sma":120,"bmi":30,"bma":35,"r":14},
        {"g":"m","ami":65,"ama":69,"smi":120,"sma":139,"bmi":30,"bma":35,"r":18},
        {"g":"m","ami":65,"ama":69,"smi":140,"sma":159,"bmi":30,"bma":35,"r":23},
        {"g":"m","ami":65,"ama":69,"smi":160,"sma":179,"bmi":30,"bma":35,"r":29},
        {"g":"m","ami":65,"ama":69,"smi":180,"sma":999,"bmi":30,"bma":35,"r":36},
        {"g":"m","ami":70,"ama":74,"smi":0,"sma":120,"bmi":30,"bma":35,"r":18},
        {"g":"m","ami":70,"ama":74,"smi":120,"sma":139,"bmi":30,"bma":35,"r":23},
        {"g":"m","ami":70,"ama":74,"smi":140,"sma":159,"bmi":30,"bma":35,"r":28},
        {"g":"m","ami":70,"ama":74,"smi":160,"sma":179,"bmi":30,"bma":35,"r":34},
        {"g":"m","ami":70,"ama":74,"smi":180,"sma":999,"bmi":30,"bma":35,"r":41},
        {"g":"m","ami":40,"ama":44,"smi":0,"sma":120,"bmi":35,"bma":999,"r":5},
        {"g":"m","ami":40,"ama":44,"smi":120,"sma":139,"bmi":35,"bma":999,"r":7},
        {"g":"m","ami":40,"ama":44,"smi":140,"sma":159,"bmi":35,"bma":999,"r":10},
        {"g":"m","ami":40,"ama":44,"smi":160,"sma":179,"bmi":35,"bma":999,"r":14},
        {"g":"m","ami":40,"ama":44,"smi":180,"sma":999,"bmi":35,"bma":999,"r":20},
        {"g":"m","ami":45,"ama":49,"smi":0,"sma":120,"bmi":35,"bma":999,"r":6},
        {"g":"m","ami":45,"ama":49,"smi":120,"sma":139,"bmi":35,"bma":999,"r":8},
        {"g":"m","ami":45,"ama":49,"smi":140,"sma":159,"bmi":35,"bma":999,"r":12},
        {"g":"m","ami":45,"ama":49,"smi":160,"sma":179,"bmi":35,"bma":999,"r":17},
        {"g":"m","ami":45,"ama":49,"smi":180,"sma":999,"bmi":35,"bma":999,"r":23},
        {"g":"m","ami":50,"ama":54,"smi":0,"sma":120,"bmi":35,"bma":999,"r":8},
        {"g":"m","ami":50,"ama":54,"smi":120,"sma":139,"bmi":35,"bma":999,"r":11},
        {"g":"m","ami":50,"ama":54,"smi":140,"sma":159,"bmi":35,"bma":999,"r":14},
        {"g":"m","ami":50,"ama":54,"smi":160,"sma":179,"bmi":35,"bma":999,"r":20},
        {"g":"m","ami":50,"ama":54,"smi":180,"sma":999,"bmi":35,"bma":999,"r":27},
        {"g":"m","ami":55,"ama":59,"smi":0,"sma":120,"bmi":35,"bma":999,"r":10},
        {"g":"m","ami":55,"ama":59,"smi":120,"sma":139,"bmi":35,"bma":999,"r":13},
        {"g":"m","ami":55,"ama":59,"smi":140,"sma":159,"bmi":35,"bma":999,"r":17},
        {"g":"m","ami":55,"ama":59,"smi":160,"sma":179,"bmi":35,"bma":999,"r":23},
        {"g":"m","ami":55,"ama":59,"smi":180,"sma":999,"bmi":35,"bma":999,"r":30},
        {"g":"m","ami":60,"ama":64,"smi":0,"sma":120,"bmi":35,"bma":999,"r":12},
        {"g":"m","ami":60,"ama":64,"smi":120,"sma":139,"bmi":35,"bma":999,"r":16},
        {"g":"m","ami":60,"ama":64,"smi":140,"sma":159,"bmi":35,"bma":999,"r":21},
        {"g":"m","ami":60,"ama":64,"smi":160,"sma":179,"bmi":35,"bma":999,"r":27},
        {"g":"m","ami":60,"ama":64,"smi":180,"sma":999,"bmi":35,"bma":999,"r":34},
        {"g":"m","ami":65,"ama":69,"smi":0,"sma":120,"bmi":35,"bma":999,"r":16},
        {"g":"m","ami":65,"ama":69,"smi":120,"sma":139,"bmi":35,"bma":999,"r":20},
        {"g":"m","ami":65,"ama":69,"smi":140,"sma":159,"bmi":35,"bma":999,"r":25},
        {"g":"m","ami":65,"ama":69,"smi":160,"sma":179,"bmi":35,"bma":999,"r":31},
        {"g":"m","ami":65,"ama":69,"smi":180,"sma":999,"bmi":35,"bma":999,"r":39},
        {"g":"m","ami":70,"ama":74,"smi":0,"sma":120,"bmi":35,"bma":999,"r":20},
        {"g":"m","ami":70,"ama":74,"smi":120,"sma":139,"bmi":35,"bma":999,"r":24},
        {"g":"m","ami":70,"ama":74,"smi":140,"sma":159,"bmi":35,"bma":999,"r":30},
        {"g":"m","ami":70,"ama":74,"smi":160,"sma":179,"bmi":35,"bma":999,"r":36},
        {"g":"m","ami":70,"ama":74,"smi":180,"sma":999,"bmi":35,"bma":999,"r":44},
        {"g":"f","ami":40,"ama":44,"smi":0,"sma":120,"bmi":0,"bma":20,"r":3},
        {"g":"f","ami":40,"ama":44,"smi":120,"sma":139,"bmi":0,"bma":20,"r":4},
        {"g":"f","ami":40,"ama":44,"smi":140,"sma":159,"bmi":0,"bma":20,"r":5},
        {"g":"f","ami":40,"ama":44,"smi":160,"sma":179,"bmi":0,"bma":20,"r":8},
        {"g":"f","ami":40,"ama":44,"smi":180,"sma":999,"bmi":0,"bma":20,"r":11},
        {"g":"f","ami":45,"ama":49,"smi":0,"sma":120,"bmi":0,"bma":20,"r":4},
        {"g":"f","ami":45,"ama":49,"smi":120,"sma":139,"bmi":0,"bma":20,"r":5},
        {"g":"f","ami":45,"ama":49,"smi":140,"sma":159,"bmi":0,"bma":20,"r":7},
        {"g":"f","ami":45,"ama":49,"smi":160,"sma":179,"bmi":0,"bma":20,"r":9},
        {"g":"f","ami":45,"ama":49,"smi":180,"sma":999,"bmi":0,"bma":20,"r":13},
        {"g":"f","ami":50,"ama":54,"smi":0,"sma":120,"bmi":0,"bma":20,"r":5},
        {"g":"f","ami":50,"ama":54,"smi":120,"sma":139,"bmi":0,"bma":20,"r":6},
        {"g":"f","ami":50,"ama":54,"smi":140,"sma":159,"bmi":0,"bma":20,"r":9},
        {"g":"f","ami":50,"ama":54,"smi":160,"sma":179,"bmi":0,"bma":20,"r":11},
        {"g":"f","ami":50,"ama":54,"smi":180,"sma":999,"bmi":0,"bma":20,"r":15},
        {"g":"f","ami":55,"ama":59,"smi":0,"sma":120,"bmi":0,"bma":20,"r":6},
        {"g":"f","ami":55,"ama":59,"smi":120,"sma":139,"bmi":0,"bma":20,"r":8},
        {"g":"f","ami":55,"ama":59,"smi":140,"sma":159,"bmi":0,"bma":20,"r":11},
        {"g":"f","ami":55,"ama":59,"smi":160,"sma":179,"bmi":0,"bma":20,"r":14},
        {"g":"f","ami":55,"ama":59,"smi":180,"sma":999,"bmi":0,"bma":20,"r":18},
        {"g":"f","ami":60,"ama":64,"smi":0,"sma":120,"bmi":0,"bma":20,"r":8},
        {"g":"f","ami":60,"ama":64,"smi":120,"sma":139,"bmi":0,"bma":20,"r":11},
        {"g":"f","ami":60,"ama":64,"smi":140,"sma":159,"bmi":0,"bma":20,"r":13},
        {"g":"f","ami":60,"ama":64,"smi":160,"sma":179,"bmi":0,"bma":20,"r":17},
        {"g":"f","ami":60,"ama":64,"smi":180,"sma":999,"bmi":0,"bma":20,"r":21},
        {"g":"f","ami":65,"ama":69,"smi":0,"sma":120,"bmi":0,"bma":20,"r":11},
        {"g":"f","ami":65,"ama":69,"smi":120,"sma":139,"bmi":0,"bma":20,"r":14},
        {"g":"f","ami":65,"ama":69,"smi":140,"sma":159,"bmi":0,"bma":20,"r":17},
        {"g":"f","ami":65,"ama":69,"smi":160,"sma":179,"bmi":0,"bma":20,"r":21},
        {"g":"f","ami":65,"ama":69,"smi":180,"sma":999,"bmi":0,"bma":20,"r":25},
        {"g":"f","ami":70,"ama":74,"smi":0,"sma":120,"bmi":0,"bma":20,"r":14},
        {"g":"f","ami":70,"ama":74,"smi":120,"sma":139,"bmi":0,"bma":20,"r":17},
        {"g":"f","ami":70,"ama":74,"smi":140,"sma":159,"bmi":0,"bma":20,"r":21},
        {"g":"f","ami":70,"ama":74,"smi":160,"sma":179,"bmi":0,"bma":20,"r":25},
        {"g":"f","ami":70,"ama":74,"smi":180,"sma":999,"bmi":0,"bma":20,"r":30},
        {"g":"f","ami":40,"ama":44,"smi":0,"sma":120,"bmi":20,"bma":24,"r":3},
        {"g":"f","ami":40,"ama":44,"smi":120,"sma":139,"bmi":20,"bma":24,"r":4},
        {"g":"f","ami":40,"ama":44,"smi":140,"sma":159,"bmi":20,"bma":24,"r":6},
        {"g":"f","ami":40,"ama":44,"smi":160,"sma":179,"bmi":20,"bma":24,"r":8},
        {"g":"f","ami":40,"ama":44,"smi":180,"sma":999,"bmi":20,"bma":24,"r":11},
        {"g":"f","ami":45,"ama":49,"smi":0,"sma":120,"bmi":20,"bma":24,"r":4},
        {"g":"f","ami":45,"ama":49,"smi":120,"sma":139,"bmi":20,"bma":24,"r":5},
        {"g":"f","ami":45,"ama":49,"smi":140,"sma":159,"bmi":20,"bma":24,"r":7},
        {"g":"f","ami":45,"ama":49,"smi":160,"sma":179,"bmi":20,"bma":24,"r":10},
        {"g":"f","ami":45,"ama":49,"smi":180,"sma":999,"bmi":20,"bma":24,"r":14},
        {"g":"f","ami":50,"ama":54,"smi":0,"sma":120,"bmi":20,"bma":24,"r":5},
        {"g":"f","ami":50,"ama":54,"smi":120,"sma":139,"bmi":20,"bma":24,"r":7},
        {"g":"f","ami":50,"ama":54,"smi":140,"sma":159,"bmi":20,"bma":24,"r":9},
        {"g":"f","ami":50,"ama":54,"smi":160,"sma":179,"bmi":20,"bma":24,"r":12},
        {"g":"f","ami":50,"ama":54,"smi":180,"sma":999,"bmi":20,"bma":24,"r":16},
        {"g":"f","ami":55,"ama":59,"smi":0,"sma":120,"bmi":20,"bma":24,"r":7},
        {"g":"f","ami":55,"ama":59,"smi":120,"sma":139,"bmi":20,"bma":24,"r":9},
        {"g":"f","ami":55,"ama":59,"smi":140,"sma":159,"bmi":20,"bma":24,"r":11},
        {"g":"f","ami":55,"ama":59,"smi":160,"sma":179,"bmi":20,"bma":24,"r":15},
        {"g":"f","ami":55,"ama":59,"smi":180,"sma":999,"bmi":20,"bma":24,"r":19},
        {"g":"f","ami":60,"ama":64,"smi":0,"sma":120,"bmi":20,"bma":24,"r":9},
        {"g":"f","ami":60,"ama":64,"smi":120,"sma":139,"bmi":20,"bma":24,"r":11},
        {"g":"f","ami":60,"ama":64,"smi":140,"sma":159,"bmi":20,"bma":24,"r":14},
        {"g":"f","ami":60,"ama":64,"smi":160,"sma":179,"bmi":20,"bma":24,"r":18},
        {"g":"f","ami":60,"ama":64,"smi":180,"sma":999,"bmi":20,"bma":24,"r":22},
        {"g":"f","ami":65,"ama":69,"smi":0,"sma":120,"bmi":20,"bma":24,"r":11},
        {"g":"f","ami":65,"ama":69,"smi":120,"sma":139,"bmi":20,"bma":24,"r":14},
        {"g":"f","ami":65,"ama":69,"smi":140,"sma":159,"bmi":20,"bma":24,"r":18},
        {"g":"f","ami":65,"ama":69,"smi":160,"sma":179,"bmi":20,"bma":24,"r":22},
        {"g":"f","ami":65,"ama":69,"smi":180,"sma":999,"bmi":20,"bma":24,"r":26},
        {"g":"f","ami":70,"ama":74,"smi":0,"sma":120,"bmi":20,"bma":24,"r":15},
        {"g":"f","ami":70,"ama":74,"smi":120,"sma":139,"bmi":20,"bma":24,"r":18},
        {"g":"f","ami":70,"ama":74,"smi":140,"sma":159,"bmi":20,"bma":24,"r":22},
        {"g":"f","ami":70,"ama":74,"smi":160,"sma":179,"bmi":20,"bma":24,"r":26},
        {"g":"f","ami":70,"ama":74,"smi":180,"sma":999,"bmi":20,"bma":24,"r":31},
        {"g":"f","ami":40,"ama":44,"smi":0,"sma":120,"bmi":25,"bma":29,"r":3},
        {"g":"f","ami":40,"ama":44,"smi":120,"sma":139,"bmi":25,"bma":29,"r":4},
        {"g":"f","ami":40,"ama":44,"smi":140,"sma":159,"bmi":25,"bma":29,"r":6},
        {"g":"f","ami":40,"ama":44,"smi":160,"sma":179,"bmi":25,"bma":29,"r":9},
        {"g":"f","ami":40,"ama":44,"smi":180,"sma":999,"bmi":25,"bma":29,"r":12},
        {"g":"f","ami":45,"ama":49,"smi":0,"sma":120,"bmi":25,"bma":29,"r":4},
        {"g":"f","ami":45,"ama":49,"smi":120,"sma":139,"bmi":25,"bma":29,"r":6},
        {"g":"f","ami":45,"ama":49,"smi":140,"sma":159,"bmi":25,"bma":29,"r":8},
        {"g":"f","ami":45,"ama":49,"smi":160,"sma":179,"bmi":25,"bma":29,"r":11},
        {"g":"f","ami":45,"ama":49,"smi":180,"sma":999,"bmi":25,"bma":29,"r":14},
        {"g":"f","ami":50,"ama":54,"smi":0,"sma":120,"bmi":25,"bma":29,"r":5},
        {"g":"f","ami":50,"ama":54,"smi":120,"sma":139,"bmi":25,"bma":29,"r":7},
        {"g":"f","ami":50,"ama":54,"smi":140,"sma":159,"bmi":25,"bma":29,"r":10},
        {"g":"f","ami":50,"ama":54,"smi":160,"sma":179,"bmi":25,"bma":29,"r":13},
        {"g":"f","ami":50,"ama":54,"smi":180,"sma":999,"bmi":25,"bma":29,"r":17},
        {"g":"f","ami":55,"ama":59,"smi":0,"sma":120,"bmi":25,"bma":29,"r":7},
        {"g":"f","ami":55,"ama":59,"smi":120,"sma":139,"bmi":25,"bma":29,"r":9},
        {"g":"f","ami":55,"ama":59,"smi":140,"sma":159,"bmi":25,"bma":29,"r":12},
        {"g":"f","ami":55,"ama":59,"smi":160,"sma":179,"bmi":25,"bma":29,"r":15},
        {"g":"f","ami":55,"ama":59,"smi":180,"sma":999,"bmi":25,"bma":29,"r":20},
        {"g":"f","ami":60,"ama":64,"smi":0,"sma":120,"bmi":25,"bma":29,"r":9},
        {"g":"f","ami":60,"ama":64,"smi":120,"sma":139,"bmi":25,"bma":29,"r":12},
        {"g":"f","ami":60,"ama":64,"smi":140,"sma":159,"bmi":25,"bma":29,"r":15},
        {"g":"f","ami":60,"ama":64,"smi":160,"sma":179,"bmi":25,"bma":29,"r":19},
        {"g":"f","ami":60,"ama":64,"smi":180,"sma":999,"bmi":25,"bma":29,"r":23},
        {"g":"f","ami":65,"ama":69,"smi":0,"sma":120,"bmi":25,"bma":29,"r":12},
        {"g":"f","ami":65,"ama":69,"smi":120,"sma":139,"bmi":25,"bma":29,"r":15},
        {"g":"f","ami":65,"ama":69,"smi":140,"sma":159,"bmi":25,"bma":29,"r":18},
        {"g":"f","ami":65,"ama":69,"smi":160,"sma":179,"bmi":25,"bma":29,"r":22},
        {"g":"f","ami":65,"ama":69,"smi":180,"sma":999,"bmi":25,"bma":29,"r":27},
        {"g":"f","ami":70,"ama":74,"smi":0,"sma":120,"bmi":25,"bma":29,"r":15},
        {"g":"f","ami":70,"ama":74,"smi":120,"sma":139,"bmi":25,"bma":29,"r":19},
        {"g":"f","ami":70,"ama":74,"smi":140,"sma":159,"bmi":25,"bma":29,"r":22},
        {"g":"f","ami":70,"ama":74,"smi":160,"sma":179,"bmi":25,"bma":29,"r":27},
        {"g":"f","ami":70,"ama":74,"smi":180,"sma":999,"bmi":25,"bma":29,"r":32},
        {"g":"f","ami":40,"ama":44,"smi":0,"sma":120,"bmi":30,"bma":35,"r":3},
        {"g":"f","ami":40,"ama":44,"smi":120,"sma":139,"bmi":30,"bma":35,"r":5},
        {"g":"f","ami":40,"ama":44,"smi":140,"sma":159,"bmi":30,"bma":35,"r":7},
        {"g":"f","ami":40,"ama":44,"smi":160,"sma":179,"bmi":30,"bma":35,"r":9},
        {"g":"f","ami":40,"ama":44,"smi":180,"sma":999,"bmi":30,"bma":35,"r":13},
        {"g":"f","ami":45,"ama":49,"smi":0,"sma":120,"bmi":30,"bma":35,"r":4},
        {"g":"f","ami":45,"ama":49,"smi":120,"sma":139,"bmi":30,"bma":35,"r":6},
        {"g":"f","ami":45,"ama":49,"smi":140,"sma":159,"bmi":30,"bma":35,"r":8},
        {"g":"f","ami":45,"ama":49,"smi":160,"sma":179,"bmi":30,"bma":35,"r":11},
        {"g":"f","ami":45,"ama":49,"smi":180,"sma":999,"bmi":30,"bma":35,"r":15},
        {"g":"f","ami":50,"ama":54,"smi":0,"sma":120,"bmi":30,"bma":35,"r":6},
        {"g":"f","ami":50,"ama":54,"smi":120,"sma":139,"bmi":30,"bma":35,"r":8},
        {"g":"f","ami":50,"ama":54,"smi":140,"sma":159,"bmi":30,"bma":35,"r":10},
        {"g":"f","ami":50,"ama":54,"smi":160,"sma":179,"bmi":30,"bma":35,"r":14},
        {"g":"f","ami":50,"ama":54,"smi":180,"sma":999,"bmi":30,"bma":35,"r":18},
        {"g":"f","ami":55,"ama":59,"smi":0,"sma":120,"bmi":30,"bma":35,"r":7},
        {"g":"f","ami":55,"ama":59,"smi":120,"sma":139,"bmi":30,"bma":35,"r":10},
        {"g":"f","ami":55,"ama":59,"smi":140,"sma":159,"bmi":30,"bma":35,"r":13},
        {"g":"f","ami":55,"ama":59,"smi":160,"sma":179,"bmi":30,"bma":35,"r":16},
        {"g":"f","ami":55,"ama":59,"smi":180,"sma":999,"bmi":30,"bma":35,"r":21},
        {"g":"f","ami":60,"ama":64,"smi":0,"sma":120,"bmi":30,"bma":35,"r":10},
        {"g":"f","ami":60,"ama":64,"smi":120,"sma":139,"bmi":30,"bma":35,"r":12},
        {"g":"f","ami":60,"ama":64,"smi":140,"sma":159,"bmi":30,"bma":35,"r":16},
        {"g":"f","ami":60,"ama":64,"smi":160,"sma":179,"bmi":30,"bma":35,"r":20},
        {"g":"f","ami":60,"ama":64,"smi":180,"sma":999,"bmi":30,"bma":35,"r":25},
        {"g":"f","ami":65,"ama":69,"smi":0,"sma":120,"bmi":30,"bma":35,"r":12},
        {"g":"f","ami":65,"ama":69,"smi":120,"sma":139,"bmi":30,"bma":35,"r":15},
        {"g":"f","ami":65,"ama":69,"smi":140,"sma":159,"bmi":30,"bma":35,"r":19},
        {"g":"f","ami":65,"ama":69,"smi":160,"sma":179,"bmi":30,"bma":35,"r":23},
        {"g":"f","ami":65,"ama":69,"smi":180,"sma":999,"bmi":30,"bma":35,"r":29},
        {"g":"f","ami":70,"ama":74,"smi":0,"sma":120,"bmi":30,"bma":35,"r":16},
        {"g":"f","ami":70,"ama":74,"smi":120,"sma":139,"bmi":30,"bma":35,"r":19},
        {"g":"f","ami":70,"ama":74,"smi":140,"sma":159,"bmi":30,"bma":35,"r":23},
        {"g":"f","ami":70,"ama":74,"smi":160,"sma":179,"bmi":30,"bma":35,"r":28},
        {"g":"f","ami":70,"ama":74,"smi":180,"sma":999,"bmi":30,"bma":35,"r":33},
        {"g":"f","ami":40,"ama":44,"smi":0,"sma":120,"bmi":35,"bma":999,"r":4},
        {"g":"f","ami":40,"ama":44,"smi":120,"sma":139,"bmi":35,"bma":999,"r":5},
        {"g":"f","ami":40,"ama":44,"smi":140,"sma":159,"bmi":35,"bma":999,"r":7},
        {"g":"f","ami":40,"ama":44,"smi":160,"sma":179,"bmi":35,"bma":999,"r":10},
        {"g":"f","ami":40,"ama":44,"smi":180,"sma":999,"bmi":35,"bma":999,"r":14},
        {"g":"f","ami":45,"ama":49,"smi":0,"sma":120,"bmi":35,"bma":999,"r":5},
        {"g":"f","ami":45,"ama":49,"smi":120,"sma":139,"bmi":35,"bma":999,"r":6},
        {"g":"f","ami":45,"ama":49,"smi":140,"sma":159,"bmi":35,"bma":999,"r":9},
        {"g":"f","ami":45,"ama":49,"smi":160,"sma":179,"bmi":35,"bma":999,"r":12},
        {"g":"f","ami":45,"ama":49,"smi":180,"sma":999,"bmi":35,"bma":999,"r":16},
        {"g":"f","ami":50,"ama":54,"smi":0,"sma":120,"bmi":35,"bma":999,"r":6},
        {"g":"f","ami":50,"ama":54,"smi":120,"sma":139,"bmi":35,"bma":999,"r":8},
        {"g":"f","ami":50,"ama":54,"smi":140,"sma":159,"bmi":35,"bma":999,"r":11},
        {"g":"f","ami":50,"ama":54,"smi":160,"sma":179,"bmi":35,"bma":999,"r":14},
        {"g":"f","ami":50,"ama":54,"smi":180,"sma":999,"bmi":35,"bma":999,"r":19},
        {"g":"f","ami":55,"ama":59,"smi":0,"sma":120,"bmi":35,"bma":999,"r":8},
        {"g":"f","ami":55,"ama":59,"smi":120,"sma":139,"bmi":35,"bma":999,"r":10},
        {"g":"f","ami":55,"ama":59,"smi":140,"sma":159,"bmi":35,"bma":999,"r":13},
        {"g":"f","ami":55,"ama":59,"smi":160,"sma":179,"bmi":35,"bma":999,"r":17},
        {"g":"f","ami":55,"ama":59,"smi":180,"sma":999,"bmi":35,"bma":999,"r":22},
        {"g":"f","ami":60,"ama":64,"smi":0,"sma":120,"bmi":35,"bma":999,"r":10},
        {"g":"f","ami":60,"ama":64,"smi":120,"sma":139,"bmi":35,"bma":999,"r":13},
        {"g":"f","ami":60,"ama":64,"smi":140,"sma":159,"bmi":35,"bma":999,"r":16},
        {"g":"f","ami":60,"ama":64,"smi":160,"sma":179,"bmi":35,"bma":999,"r":21},
        {"g":"f","ami":60,"ama":64,"smi":180,"sma":999,"bmi":35,"bma":999,"r":26},
        {"g":"f","ami":65,"ama":69,"smi":0,"sma":120,"bmi":35,"bma":999,"r":13},
        {"g":"f","ami":65,"ama":69,"smi":120,"sma":139,"bmi":35,"bma":999,"r":16},
        {"g":"f","ami":65,"ama":69,"smi":140,"sma":159,"bmi":35,"bma":999,"r":20},
        {"g":"f","ami":65,"ama":69,"smi":160,"sma":179,"bmi":35,"bma":999,"r":24},
        {"g":"f","ami":65,"ama":69,"smi":180,"sma":999,"bmi":35,"bma":999,"r":30},
        {"g":"f","ami":70,"ama":74,"smi":0,"sma":120,"bmi":35,"bma":999,"r":17},
        {"g":"f","ami":70,"ama":74,"smi":120,"sma":139,"bmi":35,"bma":999,"r":20},
        {"g":"f","ami":70,"ama":74,"smi":140,"sma":159,"bmi":35,"bma":999,"r":24},
        {"g":"f","ami":70,"ama":74,"smi":160,"sma":179,"bmi":35,"bma":999,"r":29},
        {"g":"f","ami":70,"ama":74,"smi":180,"sma":999,"bmi":35,"bma":999,"r":34}
    ];

    for (let row of data) {
        if (
            row["g"] === gender &&
            row["ami"] <= age &&
            age <= row["ama"] &&
            row["smi"] <= systolic &&
            systolic <= row["sma"] &&
            row["bmi"] <= bmi &&
            bmi <= row["bma"]
        ) {
            return row["r"];
        }
    }

    return null;
}