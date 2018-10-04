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

#ifndef ECHOSERVER_H
#define ECHOSERVER_H

#include <QObject>
#include <QTcpServer>

class EchoServer: public QObject
{
    Q_OBJECT
public:
    EchoServer(QObject* parent = nullptr);
    ~EchoServer();

    bool startServer(quint16 port);

private Q_SLOTS:
    void onNewConnection();
    void onReadReady();
    void onDisconnected();

private:
    QTcpServer *mServer;
    int mSocketCount;
};

#endif // ECHOSERVER_H
