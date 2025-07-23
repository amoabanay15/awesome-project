#!/bin/bash

# Script to backup important files

# Variables
BACKUP_DIR="/backups"
SOURCE_DIR="/important_files"
DATE=$(date +%Y-%m-%d)

# Check if backup directory exists
if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR" || { echo "Failed to create backup dir"; exit 1; }
fi

# Create backup
tar -czf "$BACKUP_DIR/backup_$DATE.tar.gz" "$SOURCE_DIR" || {
    echo "Backup failed!" >&2
    exit 1
}

echo "Backup completed successfully."