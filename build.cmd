mkdocs build
echo tpdocs.alivegamestudio.com> docs/CNAME
git commit -am "build"
git push
pause
