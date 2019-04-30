/*
 * This file is part of the Skycoin project, https://skycoin.net/
 *
 * Copyright (C) 2018-2019 Skycoin Project
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *
 */

#include <libopencm3/stm32/desig.h>

#include "skywallet.h"
#include "oled.h"
#include "bitmaps.h"
#include "util.h"
#include "usb.h"
#include "setup.h"
#include "storage.h"
#include "layout.h"
#include "layout2.h"
#include "rng.h"
#include "timer.h"
#include "buttons.h"
#include "gettext.h"
#include "fastflash.h"
#include "factory_test.h"
#include "entropy.h"
#include "memory.h"

extern uint32_t device_uuid[STM32_UUID_LEN/sizeof(uint32_t)];
int main(void)
{
#ifndef APPVER
	setup();
	__stack_chk_guard = random32(); // this supports compiler provided unpredictable stack protection checks
	oledInit();
#else
	setupApp();
	__stack_chk_guard = random32(); // this supports compiler provided unpredictable stack protection checks
#endif

#if FASTFLASH
	uint16_t state = gpio_port_read(BTN_PORT);
	if ((state & BTN_PIN_NO) == 0) {
		run_bootloader();
	}
#endif

	timer_init();

#ifdef APPVER
	set_up_rdp_level();
	desig_get_unique_id(device_uuid);
	// enable MPU (Memory Protection Unit)
	mpu_config();
#else
	random_buffer((uint8_t *)device_uuid, sizeof(device_uuid));
#endif

#if DEBUG_LINK
	oledSetDebugLink(1);
	storage_wipe();
#endif

	oledDrawBitmap(0, 0, &bmp_skycoin_logo64);
	oledRefresh();

	storage_init();
	layoutHome();
	usbInit();
	for (;;) {
		usbPoll();
		check_lock_screen();
		check_factory_test();
		check_entropy();
	}

	return 0;
}
