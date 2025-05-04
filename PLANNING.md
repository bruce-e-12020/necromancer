# PLANNING

## Steps for Every Stage of Project

1. Write a set of tasks in TASKS.md.
    --Mark each task complete as they are completed.
2. Create unit tests for every function and class created. Every new function and class should have a set of tests ready to go.
3. Run tests whenever the code changes. Rewrite tests if code change warrants it.
4. Update repo and version number regularly. 
    --Use branching to add new functionality.
        --Create a git tag locally: `git tag -a v0.1.0 -m "Initial project setup with Game class and unit tests"`
        --Push the tag to GitHub: `git push origin v0.1.0`
        --On GitHub.com:
            --Go to repository: https://github.com/bruce-e-12020/necromancer
            --Click "Create a new release"
            --Choose the tag you just pushed (v0.1.0)
            --Add a release title (e.g., "Initial Release")
            --Add release notes describing what's included (in CHANGELOG.md)