#!/bin/bash

PROFILE_PATH=$WAS_HOME_PROFILES/$PROFILE_NAME

cat <<EOT > $PROFILE_PATH/bin/updateConfig.sh
#!/bin/bash
set -e
NODE_DIR=$PROFILE_PATH/config/cells/DefaultCell01/nodes/DefaultNode01
CELL_DIR=$PROFILE_PATH/config/cells/DefaultCell01

  echo "Updating configuration with new hostname..."

  sed -i -e "s/port=\"9060\"/port=\"\$CONSOLE_PORT\"/" \$NODE_DIR/serverindex.xml
  sed -i -e "s/port=\"9060\"/port=\"\$CONSOLE_PORT\"/" \$CELL_DIR/virtualhosts.xml
  sed -i -e "s/port=\"9080\"/port=\"\$HTTP_PORT\"/" \$NODE_DIR/serverindex.xml
  sed -i -e "s/port=\"9080\"/port=\"\$HTTP_PORT\"/" \$CELL_DIR/virtualhosts.xml
  sed -i -e "s/port=\"9043\"/port=\"\$HTTPS_PORT\"/" \$NODE_DIR/serverindex.xml
  sed -i -e "s/port=\"9043\"/port=\"\$HTTPS_PORT\"/" \$CELL_DIR/virtualhosts.xml

  echo \$HOSTNAME > $PROFILE_PATH/.hostname
EOT

chmod a+x $PROFILE_PATH/bin/updateConfig.sh

# Speed up the first start of a new container
$PROFILE_PATH/bin/./updateConfig.sh

cat <<EOT > $PROFILE_PATH/bin/start.sh
#!/bin/bash
set -e
$PROFILE_PATH/bin/./updateConfig.sh
echo "Starting server..."
exec $PROFILE_PATH/bin/start_server1.sh
EOT

chmod a+x $PROFILE_PATH/bin/start.sh
