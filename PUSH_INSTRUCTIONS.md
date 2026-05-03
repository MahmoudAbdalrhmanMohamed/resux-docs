# Push Instructions

Use these commands from a machine that can reach GitHub and has permission to push to `MahmoudAbdalrhmanMohamed/resux-docs`.

```sh
unzip resux-docs.zip
cd resux-docs
npm install
npm run build
git init
git branch -M main
git remote add origin https://github.com/MahmoudAbdalrhmanMohamed/resux-docs.git
git add .
git commit -m "Add Resux documentation site"
git push -u origin main
```

After pushing, enable GitHub Pages with GitHub Actions as the source if it is not already enabled.
