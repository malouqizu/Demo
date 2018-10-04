/* Copyright (C) 2017 RDA Technologies Limited and/or its affiliates("RDA").
 * All rights reserved.
 *
 * This software is supplied "AS IS" without any warranties.
 * RDA assumes no responsibility or liability for the use of the software,
 * conveys no license or title under any patent, copyright, or mask work
 * right to the product. RDA reserves the right to make changes in the
 * software without notification.  RDA also make no representation or
 * warranty that such application will be suitable for the specified use
 * without further testing or modification.
 */

#include <QCoreApplication>
#include "echoserver.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    if (argc != 2) {
        printf("Usage: %s <port>\n\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    EchoServer* server = new EchoServer();
    if (!server->startServer(atoi(argv[1]))) {
        exit(EXIT_FAILURE);
    }

    return a.exec();
}
