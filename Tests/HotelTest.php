<?php
    require_once __DIR__ . '/../core/app/model/HabitacionData.php';
    require_once __DIR__ . '/../core/app/model/ReservaData.php';
    require_once __DIR__ . '/../core/app/model/ClienteData.php';
    use PHPUnit\Framework\TestCase;

    class HotelTest extends TestCase
    {
        private static $suiteName = "Suite 101";
        private static $suiteDescription = "Luxury Suite";
        private static $suitePrice = "200.00";
        private static $reservationStart = "2024-01-01";
        private static $reservationEnd = "2024-01-05";
        private static $clientEmail = "john@example.com";

        /**
         * @test
         * Test room creation
         */
        public function testHabitacionCreation()
        {
            $habitacion = new HabitacionData();
            $habitacion->nombre = self::$suiteName;
            $habitacion->descripcion = self::$suiteDescription;
            $habitacion->precio = self::$suitePrice;
            $habitacion->id_categoria = 1;
            $habitacion->estado = "1";
            $this->assertEquals(self::$suiteName, $habitacion->nombre);
            $this->assertEquals(self::$suiteDescription, $habitacion->descripcion);
            $this->assertEquals(self::$suitePrice, $habitacion->precio);
        }

        /**
         * @test
         * Test reservation creation
         */
        public function testReservaCreation()
        {
            $reserva = new ReservaData();
            $reserva->name = "John Doe";
            $reserva->start = self::$reservationStart;
            $reserva->end = self::$reservationEnd;
            $reserva->room_id = 1;
            $reserva->status = "1";
            $reserva->paid = "1";
            $this->assertEquals("John Doe", $reserva->name);
            $this->assertEquals(self::$reservationStart, $reserva->start);
            $this->assertEquals(self::$reservationEnd, $reserva->end);
        }

        /**
         * @test
         * Test client creation
         */
        public function testClienteCreation()
        {
            $cliente = new ClienteData();
            $cliente->nombres = "John";
            $cliente->apellidos = "Doe";
            $cliente->direccion = "123 Main St";
            $cliente->email = self::$clientEmail;
            $cliente->telefono = "123456789";
            $cliente->usuario = "johndoe";
            $cliente->password = "password123";
            $this->assertEquals("John", $cliente->nombres);
            $this->assertEquals("Doe", $cliente->apellidos);
            $this->assertEquals(self::$clientEmail, $cliente->email);
        }

        /**
         * @test
         * Test reservation validation
         */
        public function testReservaDateValidation()
        {
            $reserva = new ReservaData();
            $reserva->start = "2024-01-01";
            $reserva->end = "2024-01-05";
            $this->assertTrue(strtotime($reserva->end) > strtotime($reserva->start));
        }

        /**
         * @test
         * Test client email validation
         */
        public function testClienteEmailValidation()
        {
            $cliente = new ClienteData();
            $cliente->email = "john@example.com";
            $this->assertRegExp('/^[^@]+@[^@]+\.[^@]+$/', $cliente->email);
        }

        /**
         * @test
         * Test room price validation
         */
        public function testHabitacionPriceValidation()
        {
            $habitacion = new HabitacionData();
            $habitacion->precio = "200.00";
            $this->assertRegExp('/^\d+(\.\d{2})?$/', $habitacion->precio);
        }
    }




