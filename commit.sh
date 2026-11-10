set -e

echo "adding..."
git add .

read -p "Enter commit message: " message
git commit -m "$message"

git push -q
