# Railway Deployment Guide (Recommended)

## 🚂 Why Railway for Django?

Railway is **much better suited** for Django applications than Vercel:
- ✅ Built-in PostgreSQL database
- ✅ No serverless timeout issues
- ✅ Persistent storage
- ✅ Easy migrations
- ✅ Free $5 credit per month
- ✅ Automatic HTTPS
- ✅ Custom domains

## 🚀 Quick Deploy to Railway (5 Steps)

### Step 1: Sign Up
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub

### Step 2: Create New Project
```bash
# Option A: Using Railway CLI (Recommended)
npm i -g @railway/cli
railway login
cd finance_portfolio
railway init
railway add --database postgres

# Option B: Using Web Dashboard
# Go to railway.app/new
# Click "Deploy from GitHub repo"
# Select your repository
```

### Step 3: Add PostgreSQL Database
- In Railway dashboard: **New → Database → PostgreSQL**
- Database will auto-configure with `DATABASE_URL`

### Step 4: Configure Environment Variables
In Railway dashboard → Variables, add:
```
SECRET_KEY=your-generated-secret-key
DEBUG=False
ALLOWED_HOSTS=.railway.app
```

### Step 5: Deploy & Migrate
```bash
# Deploy
railway up

# Run migrations
railway run python manage.py migrate

# Create superuser
railway run python manage.py createsuperuser

# View your app
railway open
```

## 🎯 Railway Configuration File

Create `railway.json` (optional):
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn finance_portfolio.wsgi:application",
    "healthcheckPath": "/",
    "healthcheckTimeout": 100
  }
}
```

## 📦 Add Gunicorn

Add to `requirements.txt`:
```
gunicorn==21.2.0
```

## 🔧 Settings for Railway

Your `settings.py` is already configured! Just ensure:
```python
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1,.railway.app').split(',')
```

## ✅ Benefits Over Vercel

| Feature | Railway | Vercel |
|---------|---------|--------|
| Database | ✅ Included | ❌ External required |
| Timeout | ✅ None | ❌ 10-60 seconds |
| Storage | ✅ Persistent | ❌ Ephemeral |
| Django Support | ✅ Excellent | ⚠️ Limited |
| Migrations | ✅ Easy | ⚠️ Manual |
| Price | ✅ $5/month free | ✅ Free tier |

## 🎓 Full Deployment Steps

1. **Prepare Code**
```bash
# Already done! Your code is ready
```

2. **Push to GitHub**
```bash
git init
git add .
git commit -m "Ready for Railway"
git remote add origin https://github.com/yourusername/finance-portfolio.git
git push -u origin main
```

3. **Deploy to Railway**
```bash
railway login
railway init
railway add postgres
railway up
```

4. **Setup Database**
```bash
railway run python manage.py migrate
railway run python manage.py createsuperuser
```

5. **Done!** 🎉
```bash
railway open
```

## 🌐 Custom Domain

Add your domain in Railway dashboard:
1. Settings → Domains
2. Add your domain
3. Update DNS records
4. Update `ALLOWED_HOSTS` in environment variables

## 💰 Pricing

- **Free**: $5 credit/month (renews monthly)
- **Hobby**: $5/month base + usage
- **Pro**: $20/month base + usage

Most apps stay within free tier!

## 📊 Monitoring

Railway provides:
- Real-time logs
- Metrics dashboard
- Deployment history
- Database backups

## 🆘 Troubleshooting

### Build fails
```bash
# Check logs in Railway dashboard
railway logs
```

### Database connection issues
```bash
# Verify DATABASE_URL is set
railway variables
```

### Static files not loading
```bash
# Run collectstatic
railway run python manage.py collectstatic --noinput
```

## 🎯 Recommended: Railway

For this Django Finance Portfolio Manager, **Railway is the best choice** because:
1. Simple one-command deployment
2. Included PostgreSQL database
3. No timeout issues
4. Easy migrations
5. Better Django support

Deploy now: [railway.app/new](https://railway.app/new) 🚀
