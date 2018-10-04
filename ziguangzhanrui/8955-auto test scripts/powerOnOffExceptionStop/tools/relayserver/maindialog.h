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

#ifndef MAINDIALOG_H
#define MAINDIALOG_H

#include <QDialog>
#include <QPushButton>
#include <QLabel>
#include <QTcpServer>

namespace Ui
{
class MainDialog;
}

struct usb_relay_device_info;
struct usb_relay_channel {
    struct usb_relay_device_info* info;
    int channel;
};

enum RelayStatus {
    RELAY_OPEN,
    RELAY_CLOSE,
    RELAY_NONE
};

class MainDialog : public QDialog
{
    Q_OBJECT

public:
    explicit MainDialog(QWidget *parent = 0);
    ~MainDialog();

private Q_SLOTS:
    void onToggleServer();
    void onToggleChannel();
    void onNewConnection();
    void onReadyRead();
    void onDisconnected();
    void onScanDevice();

private:
    QList<usb_relay_channel> scanChannels();
    void setChannel(int n, RelayStatus oc, const QString& name);
    void ctrlChannel(int n, RelayStatus oc);

    Ui::MainDialog *ui;

    QList<QPushButton*> mButtons;
    QList<QLabel*> mLabels;
    QTcpServer* mServer;
    QList<usb_relay_channel> mChannels;
    struct usb_relay_device_info* mDeviceInfo;
};

#endif // MAINDIALOG_H
