<pre>
        # HOW TO ADD SWAP SPACE ON CENTOS 7
            1) sudo swapon --show
        ## CREATING A SWAP FILE with  sudo privileges
            2) sudo dd if=/dev/zero of=/swapfile bs=1024 count=1048576 -- this is for 1Gb for chef we need almost 2GB
        * Ensure that only the root user can read and write the swap file:
           3) sudo chmod 600 /swapfile
        * Next, set up a Linux swap area on the file:
            4) sudo mkswap /swapfile
        * Run the following command to activate the swap:
            5) sudo swapon /swapfile
        * Make the change permanent by opening the /etc/fstab file:
            6) /swapfile swap swap defaults 0 0 --- add at the bootom of the file
        * Verify that the swap is active by using either the swapon or the free command as shown below:
            7) sudo swapon --show
            8) sudo free -h
        ## WHILE THE SWAPPINESS VALUE OF 30 IS OK FOR DESKTOP AND DEVELOPMENT MACHINES, FOR PRODUCTION SERVERS YOU MAY NEED TO SET A LOWER VALUE.
            FOR EXAMPLE, TO SET THE SWAPPINESS VALUE TO 10, TYPE:
            sudo sysctl vm.swappiness=10
        * To make this parameter persistent across reboots append the following line to the /etc/sysctl.conf file:
           vm.swappiness=10
       ----------------------------------------------------------------------------------------------------
       # HOW TO CREATE A SUDO USER ON CENTOS
         * Start by logging in to your CentOS server as the root user.
            1) ssh root@server_ip_address
         * Create a new user account using the useradd command
            2) useradd username
         * Use the passwd command to set a password for the new user.
            3) passwd username
         * Add the new user to the wheel group.
            4) usermod -aG wheel username
         * Switch to the newly created user:
            5) su - username
         * To use sudo, simply prefix the command with sudo and space.
            6) sudo [COMMAND]
         * For example, to list the contents of the /root directory you would use:
            7) sudo ls -l /root
            






</pre>