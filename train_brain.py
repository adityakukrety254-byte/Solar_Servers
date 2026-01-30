import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np
print("SOLARSERVER AI TRAINER")
print("=" * 40)
url = "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain+.txt"
cols = ['duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','hot','num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations','num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count','serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count','dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate','label','difficulty']
try:
    print("Downloading dataset...")
    df = pd.read_csv(url, names=cols, header=None)
    print(f"Loaded {len(df)} samples")
    X = df[['src_bytes','dst_bytes','count','srv_count','dst_host_count']].values
except:
    print("Download failed, using synthetic data...")
    np.random.seed(42)
    n = 5000
    X = np.column_stack([np.random.choice([80,443,8080,3306],n),np.random.exponential(1000,n),np.random.exponential(5000,n),np.random.randint(1,50,n),np.random.choice([0,1],n,p=[0.3,0.7])])
    print(f"Generated {n} samples")
print("\nTraining...")
sc = StandardScaler()
Xs = sc.fit_transform(X)
clf = IsolationForest(n_estimators=100,contamination=0.01,random_state=42,n_jobs=-1)
clf.fit(Xs)
joblib.dump(clf,"SolarServer_model.pkl")
joblib.dump(sc,"SolarServer_scaler.pkl")
print("Model saved")
print("\nTesting...")
t1 = [[443,1000,5000,10,1]]
t2 = [[6666,50000,100,1,0]]
print(f"   Normal: {'SAFE' if clf.predict(sc.transform(t1))[0]==1 else 'THREAT'}")
print(f"   Suspicious: {'SAFE' if clf.predict(sc.transform(t2))[0]==1 else 'THREAT'}")
