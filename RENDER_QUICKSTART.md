# 🚀 Deploy to Render in 10 Minutes (FREE)

**No credit card required!**

## Step 1: Push to GitHub (2 min)

```bash
cd finance_portfolio
git init
git add .
git commit -m "Deploy to Render"
git remote add origin https://github.com/YOUR_USERNAME/finance-portfolio.git
git push -u origin main
```

## Step 2: Create Render Account (1 min)

1. Go to [render.com](https://render.com)
2. Click "Get Started"
3. Sign up with GitHub
4. ✅ **No credit card needed!**

## Step 3: Create Database (2 min)

1. Dashboard → **New +** → **PostgreSQL**
2. Settings:
   - Name: `finance-db`
   - Database: `finance_db`
   - Plan: **Free**
3. **Create Database**
4. **Copy "Internal Database URL"** (save it!)

## Step 4: Create Web Service (3 min)

1. Dashboard → **New +** → **Web Service**
2. Connect your GitHub repo
3. Settings:
   - Name: `finance-portfolio`
   - Runtime: **Python 3**
   - Build Command:
     ```
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   - Start Command:
     ```
     gunicorn finance_portfolio.wsgi:application
     ```
   - Plan: **Free**

## Step 5: Environment Variables (2 min)

Click **"Advanced"** → Add these:

| Key | Value |
|-----|-------|
| SECRET_KEY | Run: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| DEBUG | `False` |
| ALLOWED_HOSTS | `.onrender.com` |
| DATABASE_URL | Paste from Step 3 |

## Step 6: Deploy! (5-10 min)

1. Click **"Create Web Service"**
2. Wait for build to complete
3. Your app will be at: `https://finance-portfolio.onrender.com`

## Step 7: Create Admin Account (1 min)

1. In Render dashboard → Your service → **Shell** tab
2. Run:
```bash
python manage.py createsuperuser
```
3. Follow prompts

## ✅ Done!

Visit: `https://your-app-name.onrender.com`

Login with your superuser account!

---

## 💡 Quick Tips

- **Slow first load?** Normal! App sleeps after 15 min
- **Keep awake:** Use [uptimerobot.com](https://uptimerobot.com) (free)
- **Database expires:** After 90 days, create new one (free again)

## 🆘 Issues?

Check `FREE_DEPLOYMENT.md` for detailed troubleshooting.

---

**Total Cost: $0.00 | Time: 10-15 minutes | Credit Card: Not needed** ✨
